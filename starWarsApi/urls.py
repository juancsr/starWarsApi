from django.contrib import admin
from django.urls import path
from rest_framework import routers
from products import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('rest_frameworks_urls', namespace='rest_framework'))
]
