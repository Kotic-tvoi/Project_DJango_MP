from django.shortcuts import render


"""Главная страница со всеми товарами."""
def index(request):
    template = 'price/index.html'
    posts = ...
    context = {'posts': posts}
    return render(request, template, context)


"""Подробная информация о товаре."""
def product_detail(request):
    template = '...'
    posts = ...
    context = {'posts': posts}
    return render(request, template, context)


"""Страница с информацией по категории товара."""
def category_products(request):
    template = '...'
    posts = ...
    context = {'posts': posts}
    return render(request, template, context)
