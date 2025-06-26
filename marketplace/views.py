from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.conf import settings
from django import forms
from .forms import OrderForm
from .models import Product, Order , CartItem
from .forms import (
    UserRegistrationForm, FarmerProfileForm, BuyerProfileForm,
    ContactForm, CropInputForm, YieldPredictionForm, ProductForm
)
from .models import (
    FarmerProfile, BuyerProfile, Crop, CropPrice, Product
)

import os
import pickle
import pandas as pd

# # Homepage View

def home(request):
    return render(request, 'marketplace/index.html')

from django.http import HttpResponse

# Custom registration form using built-in User model
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            # role = form.cleaned_data['role']
            role = request.POST.get('role')
            if not role:
                messages.error(request, "Please select a role (Farmer or Buyer).")
                return redirect('register')
            user.set_password(raw_password)
            user.save()
            UserProfile.objects.create(user=user, role=role)
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'marketplace/register.html', {'user_form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            role = UserProfile.objects.get(user=user).role
            if role == 'farmer':
                return redirect('farmer_dashboard')
            elif role == 'buyer':
                return redirect('buyer_dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'marketplace/login.html', {'form': ''})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
    
@login_required
def farmer_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    if profile.role != 'farmer':
        return redirect('login')
    return render(request, 'marketplace/farmer_dashboard.html', {'is_farmer': True})

@login_required
def buyer_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    if profile.role != 'buyer':
        return redirect('login')
    return render(request, 'marketplace/buyer_dashboard.html', {'is_farmer': False})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Add to CartItem instead of Order
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
    
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    
    cart_item.save()
    return redirect('product_list')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    # Add total price per item manually
    for item in cart_items:
        item.item_total_price = item.product.price_per_unit * item.quantity
    
    total_price = sum(item.item_total_price for item in cart_items)

    return render(request, 'direct-selling/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


@login_required
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


@login_required
def delete_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')


# @login_required
# def place_order(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     if request.method == "POST":
#         quantity = int(request.POST.get('quantity', 1))  # default to 1 if not provided

#         # Always create a new order, allowing multiple orders of same product
#         Order.objects.create(
#             buyer=request.user,
#             product=product,
#             quantity=quantity
#         )
#         return redirect('order_success')  # Replace with your success page

#     return render(request, 'direct-selling/place_order.html', {'product': product})

# Place order for one product from cart
@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

    for item in cart_items:
        order = Order.objects.create(
            buyer=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.product.price_per_unit * item.quantity
        )
        order.save()

    cart_items.delete()
    messages.success(request, "✅ Your order has been placed successfully.")
    return redirect('order_success')

@login_required  
def order_success(request):
    return render(request, 'direct-selling/order_success.html')

@login_required
def my_orders(request):
    orders = Order.objects.filter(buyer=request.user).order_by('-created_at')
    return render(request, 'direct-selling/my_orders.html', {'orders': orders})


# Show orders of current user as a seller (if user sold any products)
@login_required
def farmer_orders(request):
    orders = Order.objects.filter(product__seller=request.user).order_by('-created_at')
    return render(request, 'direct-selling/farmer_orders.html', {'orders': orders})

@login_required
def my_products(request):
    products = Product.objects.filter(seller=request.user)  # or farmer=request.user
    return render(request, 'direct-selling/my_products.html', {'products': products})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('my_products')  # Go back to My Products
    else:
        form = ProductForm(instance=product)

    return render(request, 'direct-selling/edit_product.html', {'form': form, 'product': product})


# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             if 'farmer' in request.POST:
#                 user.save()
#                 messages.success(request, "Farmer registered successfully.")
#             elif 'buyer' in request.POST:
#                 user.save()
#                 messages.success(request, "Buyer registered successfully.")
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'marketplace/register.html', {'user_form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # update with your dashboard/home route
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'marketplace/login.html', {'form': form})


# # User Registration (Farmers and Buyers)
# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user.password)
#             user.save()

#             if 'farmer' in request.POST:
#                 farmer_form = FarmerProfileForm(request.POST)
#                 if farmer_form.is_valid():
#                     farmer_profile = farmer_form.save(commit=False)
#                     farmer_profile.user = user
#                     farmer_profile.save()
#             elif 'buyer' in request.POST:
#                 buyer_form = BuyerProfileForm(request.POST)
#                 if buyer_form.is_valid():
#                     buyer_profile = buyer_form.save(commit=False)
#                     buyer_profile.user = user
#                     buyer_profile.save()

#             return redirect('home')
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'marketplace/register.html', {'user_form': user_form})

# # Login View
# def custom_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # redirect to home or dashboard
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'marketplace/login.html', {'form': form})


# Profile View
@login_required
def profile(request):
    try:
        profile = FarmerProfile.objects.get(user=request.user)
    except FarmerProfile.DoesNotExist:
        profile = None
    return render(request, 'marketplace/profile.html', {'profile': profile})

# Crop Price View
@login_required
def crop_price_view(request):
    crop_prices = CropPrice.objects.all().order_by('crop_name')
    return render(request, 'marketplace/crop_price.html', {'crop_prices': crop_prices})

# Load Crop Prediction Models
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models', 'minmaxscaler.pkl')
model_path = os.path.join(settings.BASE_DIR, 'ml_models', 'model.pkl')

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

with open(model_path, 'rb') as f:
    model = pickle.load(f)

LABEL_TO_CROP = {
    1: 'rice', 2: 'maize', 3: 'jute', 4: 'cotton', 5: 'coconut',
    6: 'papaya', 7: 'orange', 8: 'apple', 9: 'muskmelon', 10: 'watermelon',
    11: 'grapes', 12: 'mango', 13: 'banana', 14: 'pomegranate', 15: 'lentil',
    16: 'blackgram', 17: 'mungbean', 18: 'mothbeans', 19: 'pigeonpeas',
    20: 'kidneybeans', 21: 'chickpea', 22: 'coffee'
}

@login_required
def predict_crop(request):
    result = None
    input_values = None
    if request.method == 'POST':
        form = CropInputForm(request.POST)
        if form.is_valid():
            input_values = form.cleaned_data
            data = [
                input_values['nitrogen'],
                input_values['phosphorus'],
                input_values['potassium'],
                input_values['pH'],
                input_values.get('temperature', 0),
                input_values.get('humidity', 0),
                input_values.get('rainfall', 0)
            ]
            scaled_data = scaler.transform([data])
            prediction = model.predict(scaled_data)[0]
            result = LABEL_TO_CROP.get(prediction, 'Unknown Crop')
            form = CropInputForm()
    else:
        form = CropInputForm()
    return render(request, 'marketplace/predict_crop.html', {
        'form': form,
        'result': result,
        'input_values': input_values
    })

# Yield Prediction
model_path = os.path.join(settings.BASE_DIR, 'ml_models', 'dtr.pkl')
preprocessor_path = os.path.join(settings.BASE_DIR, 'ml_models', 'preprocessor.pkl')

with open(model_path, 'rb') as f:
    yield_model = pickle.load(f)

with open(preprocessor_path, 'rb') as f:
    preprocessor = pickle.load(f)

@login_required
def yeild_predict(request):
    prediction = None
    entered_data = None
    if request.method == 'POST':
        form = YieldPredictionForm(request.POST)
        if form.is_valid():
            entered_data = form.cleaned_data
            data = {
                'Year': entered_data['year'],
                'average_rain_fall_mm_per_year': entered_data['average_rain_fall_mm_per_year'],
                'pesticides_tonnes': entered_data['pesticides_tonnes'],
                'avg_temp': entered_data['avg_temp'],
                'Area': entered_data['area'],
                'Item': entered_data['item']
            }
            data_df = pd.DataFrame([data])
            X = preprocessor.transform(data_df)
            prediction = round(yield_model.predict(X)[0], 2)
            form = YieldPredictionForm()
    else:
        form = YieldPredictionForm()

    return render(request, 'marketplace/yield_predict.html', {
        'form': form,
        'prediction': prediction,
        'entered_data': entered_data
    })

# Contact View
@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for contacting us. We will get back to you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'marketplace/contact.html', {'form': form})

# Product Upload
@login_required
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'direct-selling/upload_product.html', {'form': form})

# Product Listing
def product_list(request):
    products = Product.objects.all().order_by('-posted_on')
    return render(request, 'direct-selling/product_list.html', {'products': products})

# Product Detail View
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'direct-selling/product_detail.html', {'product': product})
