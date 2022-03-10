from django.urls import path, include
from rest_framework import routers

from some_app.views import ProductViewSet, ProductGet

router = routers.DefaultRouter()

router.register('products', ProductViewSet, basename='products')

urlpatterns = (
    path('', include(router.urls)),
    path('custom/', ProductGet.as_view(), name='custom'),
)
