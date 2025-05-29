from django.contrib import admin
from django.urls import path
from marketplace import views
from marketplace.views import contact_view
from django.conf import settings
from django.conf.urls.static import static
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin12/', admin.site.urls),
    path('', views.home, name='home'),  # Homepage
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
         
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('profile/', views.profile, name='profile'),  # User Profile 
    path('predict-crop/', views.predict_crop, name='predict_crop'),
    path('yeild-predict/', views.yeild_predict, name='yeild_predict'),
    path('contact/', views.contact_view, name='contact'),
    path('crop_price/', views.crop_price_view, name='crop_prices'),
    path('direct-selling/upload/', views.upload_product, name='upload_product'),
    path('direct-selling/', views.product_list, name='product_list'),
    path('direct-selling/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('order/success/', views.order_success, name='order_success'),

    path('my_orders/', views.my_orders, name='my_orders'),
    path('farmer_orders/', views.farmer_orders, name='farmer_orders'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('farmer/my-products/', views.my_products, name='my_products'),

    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)