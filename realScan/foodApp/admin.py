from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import Ingredient

class IngredientAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Ingredient, IngredientAdmin)