from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .serializers import *
from rest_framework.response import Response
# Create your views here.
class OrderCreateApiView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(status='active')
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "order_group",
                {
                    "type": "add_new_order",
                },
            )
            return Response(serializer.data)
        return Response(serializer.errors)