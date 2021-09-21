# coding: utf-8
from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from .views.manufacturer_views import ManufacturerViewSet
from .views.product_views import ProductViewSet
from .views.order_views import OrderViewSet

app_name = "some_api"

router = routers.DefaultRouter()
router.register(r"manufacturers", ManufacturerViewSet)
router.register(r"products", ProductViewSet)
router.register(r"orders", OrderViewSet)
urlpatterns = [
    url(r"^", include(router.urls)),
]
