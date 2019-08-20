from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products_catelog, name='all_products'),
    path('<slug:c_slug>/', views.all_products_catelog,
         name='products_by_category'),

]
