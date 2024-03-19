from django.contrib import admin
from . models import userinfo, productCategory, products

# Register your models here.

admin.site.register(userinfo)
admin.site.register(productCategory)
admin.site.register(products)