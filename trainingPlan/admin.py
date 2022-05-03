from django.contrib import admin
from .models.models import Category, Plan

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Plan)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price',]

    prepopulated_fields = {'slug': ('title',)}