"""
URL mappings for the order app
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet

router = DefaultRouter()
router.register("payment", PaymentViewSet)

app_name = "payment"

urlpatterns = [
    path("", include(router.urls)),
]
