from django.urls import path
from . import views
from django.urls import path, include  # Include the 'include' function
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shopping'  # Optional namespace for URLs

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='api'),
    path('', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
  # URL for product list view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

