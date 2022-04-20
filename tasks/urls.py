from django.urls import path
from .views import CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls
