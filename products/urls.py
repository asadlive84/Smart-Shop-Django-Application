from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views

router = DefaultRouter()

router.register(r'product-list', views.ProductListView)


app_label = "product"

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name="product_list"),
    path('list/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('list/create/', views.ProductCreateView.as_view(), name="product_create"),
    path('category/', views.ProductCategoryListView.as_view(), name="product_category_list"),
    path('category/<int:pk>/', views.ProductCategoryDetailView.as_view(), name="product_category_detail"),
    path('category/create/', views.ProductCategoryCreateView.as_view(), name="product_category_create"),
]