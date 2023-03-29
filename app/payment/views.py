from django.shortcuts import render

# Create your views here.
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Payment

from .serializers import PaymentSerializer

@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name="order_id",
                type=OpenApiTypes.NUMBER,
                location=OpenApiParameter.QUERY,
                description="Filter by order id",
            ),
        ],
    ),
    # retrieve=extend_schema(
    #     parameters=[
    #         OpenApiParameter(
    #             name="name",
    #             type=OpenApiTypes.STR,
    #             location=OpenApiParameter.QUERY,
    #             description="Filter by name",
    #         ),
    #         OpenApiParameter(
    #             name="tags",
    #             type=OpenApiTypes.STR,
    #             location=OpenApiParameter.QUERY,
    #             description="Filter by tags",
    #         ),
    #     ],
    # ),
)
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = self.queryset
        order_id = self.request.query_params.get("order_id")
        if order_id:
            queryset = queryset.filter(order_id=order_id)
        return queryset.filter(user_id=self.request.user.id).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    @action(detail=True, methods=["put"])
    def success(self, request, pk=None):
        payment = self.get_object()
        payment.payment_status = "SUCCESS"
        payment.save()
        return Response(status=status.HTTP_200_OK)
