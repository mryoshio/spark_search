from django.contrib import admin

from .models import Image, ProductGroup, Language, Publisher, Item

admin.site.register(Image)
admin.site.register(ProductGroup)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Item)
