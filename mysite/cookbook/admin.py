from django.contrib import admin
from .models import Contributor, Recipe, RecipeType

# Register your models here.
admin.site.register(Contributor)
admin.site.register(RecipeType)
admin.site.register(Recipe)
