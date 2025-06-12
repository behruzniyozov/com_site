from django.contrib import admin

from products.models import *


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category", "is_active")
    list_display_links = ("id", "name", "brand")
    list_filter = ("is_active", "brand", "category")
    search_fields = ("name", "brand", "category")
    list_editable = ("is_active",)

    inlines = [ProductVariantInline]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo")
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
 
@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "user", "rating", "created_at")
    list_display_links = ("id", "product", "user")
    search_fields = ("product__name", "user__username")
    list_filter = ("rating", "created_at")
    readonly_fields = ("created_at",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "user", "text", "created_at")
    list_display_links = ("id", "product", "user")
    search_fields = ("product__name", "user__username", "text")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
    