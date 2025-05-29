from django import forms
from django.contrib.auth.forms import User, UserCreationForm
from .models import FarmerProfile, BuyerProfile, Crop,Contact,Product
from .models import Order

# ✅ Updated Registration Form using Django's built-in UserCreationForm
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    ROLE_CHOICES = (
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# Farmer Profile Form
class FarmerProfileForm(forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ['farm_name', 'location', 'contact_number']

# Buyer Profile Form
class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model = BuyerProfile
        fields = ['company_name', 'contact_number']

class CropInputForm(forms.Form):
    nitrogen = forms.FloatField(label='Nitrogen (%)')
    phosphorus = forms.FloatField(label='Phosphorus (%)')
    potassium = forms.FloatField(label='Potassium (%)')
    pH = forms.FloatField(label='pH Level')
    temperature = forms.FloatField(label='Temperature (°C)', required=False)
    humidity = forms.FloatField(label='Humidity (%)', required=False)
    rainfall = forms.FloatField(label='Rainfall (mm)', required=False)  



from django import forms

class YieldPredictionForm(forms.Form):
    year = forms.IntegerField(label='Year')
    average_rain_fall_mm_per_year = forms.FloatField(label='Average Rainfall (mm/year)')
    pesticides_tonnes = forms.FloatField(label='Pesticides (tonnes)')
    avg_temp = forms.FloatField(label='Average Temperature (°C)')
    area = forms.CharField(label='Area', max_length=100)
    item = forms.CharField(label='Crop Item', max_length=100)



# farm_app/forms.py
# contact page form
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']



# Product form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'price_per_unit', 'location', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1})
        }
        