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

    path('tag/', views.ProductTagListView.as_view(), name="product_tag_list"),
    path('tag/<int:pk>/', views.ProductTagDetialView.as_view(), name="product_tag_detail"),
    path('tag/create/', views.ProductTagCreateView.as_view(), name="product_tag_create"),

    path('vendor/', views.VendorListView.as_view(), name="vendor_list"),
    path('vendor/<int:pk>/', views.VendorDetialView.as_view(), name="vendor_detail"),
    path('vendor/create/', views.VendorDetialView.as_view(), name="vendor_create"),

    path('unit/', views.ProductUnitListView.as_view(), name="unit_list"),
    path('unit/<int:pk>/', views.ProductUnitDetialView.as_view(), name="unit_detail"),
    path('unit/create/', views.ProductUnitCreateView.as_view(), name="unit_create"),
]
