from django.contrib import admin

from price.models import Category, Product

admin.site.empty_value_display = 'Не задано'


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'article',
        'article_wb',
        'article_ozon',
        'category',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('article', 'name')
    list_filter = ('category',)
    list_display_links = ('name',)


class ProductInline(admin.StackedInline):
    model = Product
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        ProductInline,
    )
    list_display = (
        'title',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
