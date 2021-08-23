from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path(
        'edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('add/', views.add_product, name="add_product"),
    path('edit/<int:product_id>/', views.edit_product, name="edit_product"),
]
