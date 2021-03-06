from django.urls import include, path
from rest_framework import routers

from .views.manufacturer_views import ManufacturerViewSet
from .views.order_views import (
    CreateOrderView,
    DestroyOrderView,
    ListOrderView,
    RetrieveOrderView,
    UpdateOrderView,
)
from .views.product_views import ListProductView, ProductViewSet, RetrieveProductView

app_name = "some_api"

router = routers.DefaultRouter()
router.register(r"manufacturers", ManufacturerViewSet)
router.register(r"products", ProductViewSet)
urlpatterns = [
    path(r"", include(router.urls)),
    path(r"order/list/", ListOrderView.as_view()),
    path(r"order/create/", CreateOrderView.as_view()),
    path(r"order/<str:pk>/", RetrieveOrderView.as_view()),
    path(r"order/<str:pk>/update/", UpdateOrderView.as_view()),
    path(r"order/<str:pk>/destroy/", DestroyOrderView.as_view()),
    path(r"product/list/", ListProductView.as_view()),
    path(r"product/<str:pk>/", RetrieveProductView.as_view()),
]
