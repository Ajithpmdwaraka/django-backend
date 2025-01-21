from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER


class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(
                {
                    "data": serializer.data,
                    "message": "Order Data Fetched Successfully",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "data": {},
                    "message": "Something went wrong while fetching order data",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)

            if not serializer.is_valid():
                return Response(
                    {"data": serializer.errors, "message": "Something went wrong"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            subject = "New order is placed"
            message = (
                "Dear customer "
                + data["customer_name"]
                + ", your order is placed. It will be delivered to your destination as soon as possible. "
                "Thanks for your order! 😍"
            )
            email = data["customer_email"]
            recipient_list = [email]
            send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)

            serializer.save()
            return Response(
                {"data": serializer.data, "message": "Order Created Successfully"},
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response(
                {"data": {}, "message": "Something went wrong in creating the order"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get("id"))

            if not order.exists():
                return Response(
                    {
                        "data": {},
                        "message": "Order is not found with this ID",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = OrderSerializer(order[0], data=data, partial=True)
            if not serializer.is_valid():
                return Response(
                    {
                        "data": serializer.errors,
                        "message": "Something went wrong",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "message": "Order is Updated Successfully",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "data": {},
                    "message": "Something went wrong in updating the order",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get("id"))

            if not order.exists():
                return Response(
                    {
                        "data": {},
                        "message": "Order is not found with this ID",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            order[0].delete()
            return Response(
                {
                    "data": {},
                    "message": "Order is deleted Successfully",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "data": {},
                    "message": "Something went wrong in deletion of the order",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
