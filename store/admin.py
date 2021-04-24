from django.contrib import admin
from .models import Category, Product, Profile, PaymentMethod


class PaymentMethodAdmin(admin.ModelAdmin):
    model = PaymentMethod
    readonly_fields = ['timestamp']
    fields = ['title', 'status', 'logo', 'slug', 'timestamp']
    list_display = ['id', 'title', 'status', 'timestamp']
    list_display_links = ['id', 'title']

admin.site.register(PaymentMethod, PaymentMethodAdmin)


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ('title', 'slug')
    list_display = ('id', 'title', 'slug',)
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    fields = ('category', 'title', 'slug', 'price', 'description', 'seller', 'status')
    list_display = ('id', 'title', 'category', 'price', 'seller', 'status', 'timestamp')
    list_display_links = ('id', 'title')
    inlines = [ProfileInline]

admin.site.register(Product, ProductAdmin)
