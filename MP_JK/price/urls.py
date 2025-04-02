from django.urls import path

from price import views

app_name = 'price'

urlpatterns = [
    path('', views.index, name='index'),
    path('/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/',
         views.category_products,
         name='category_products'),
 
]
