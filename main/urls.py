from django.urls import path
from .views import CategoryListCreate, ProductListCreate, ProductDetail, ProductByCategory, SearchAPIView

urlpatterns = [
    path('api/categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/products/category/<int:category_id>/', ProductByCategory.as_view(), name='products-by-category'),
    path('search/', SearchAPIView.as_view(), name='search'),
]
