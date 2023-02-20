from django.urls import path, include
from rest_framework import routers

from some_app.views import (
    ProductViewSet,
    ProductsValues,
    ForLoopObjects,
    ForLoopValues,
    ProductsValuesViewSet,
    SQLDebugV1,
    SQLDebugV2,
    SQLDebugV3,
    products_values,
    products_values_async,
)

router = routers.DefaultRouter()

router.register("v1", ProductViewSet, basename="v1")
router.register("v2", ProductsValuesViewSet, basename="v2")

urlpatterns = (
    path("", include(router.urls)),
    path("v3/", ProductsValues.as_view(), name="v3"),
    path("v3_2/", products_values, name="v3_2"),
    path("v3_3/", products_values_async, name="v3_3"),
    path("v4/", ForLoopObjects.as_view(), name="v4"),
    path("v5/", ForLoopValues.as_view(), name="v5"),
    path("sql_debug_v1/", SQLDebugV1.as_view(), name="sql_debug_v1"),
    path("sql_debug_v2/", SQLDebugV2.as_view(), name="sql_debug_v2"),
    path("sql_debug_v3/", SQLDebugV3.as_view(), name="sql_debug_v3"),
)
