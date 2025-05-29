from django.contrib import admin
from .models import FarmerProfile, Crop, BuyerProfile,CropPrice,Contact,Product,Order,CartItem

admin.site.register(FarmerProfile)
admin.site.register(Crop)
admin.site.register(BuyerProfile)
admin.site.register(CropPrice)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CartItem)
