from django.contrib import admin
from caterogries.models import (
    Category,
    CategoryImage
)

admin.site.register(Category)
admin.site.register(CategoryImage)
