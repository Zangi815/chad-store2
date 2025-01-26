from django.contrib import admin
from products.models import (
    Product,
    ProductImage,
    ProductTag,
    FavoriteProduct,
    Review,
    Cart
)

class ImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 0
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInLine]

admin.site.register(ProductImage)
admin.site.register(ProductTag)
admin.site.register(FavoriteProduct)
admin.site.register(Review)
admin.site.register(Cart)

