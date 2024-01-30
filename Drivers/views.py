from django.shortcuts import render
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class OperatorTokenApiView(APIView):
    @swagger_auto_schema(request_body=CustomOperatorSerializer)
    def post(self, request):
        operator = CustomUser.objects.filter(
            username = request.data.get('username'),
            password = request.data.get('password'),
            role = 'operator'
        ).first()
        if operator is None:
            return Response({"xabar": "Operator topilmadi"})
        refresh = RefreshToken.for_user(operator)
        resp = {
            "username" : request.data.get('username'),
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return Response(resp)

class DriverTokenApiView(APIView):
    @swagger_auto_schema(request_body=CustomOperatorSerializer)
    def post(self, request):
        driver = CustomUser.objects.filter(
            username=request.data.get('username'),
            role='driver'
        ).first()
        if driver is None:
            return Response({"xabar": "Operator topilmadi"})
        refresh = RefreshToken.for_user(driver)
        resp = {
            "username": request.data.get('username'),
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return Response(resp)

class DriversApiView(APIView):
    def get(self, request):
        driver = Driver.objects.all()
        serializer = DriverSerialzer(driver, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = DriverSerialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DriverApiView(APIView):
    def update(self, request, pk):
        data = request.data
        driver = Driver.objects.get(id=pk)
        serializer = DriverSerialzer(driver, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        Driver.objects.get(id=pk).delete()
        return Response({'success': 'True'})

class CarCategoryApiView(APIView):
    def get(self, request):
        category = CarCategory.objects.all(many=True)
        serializer = CarCategorySerializer(category, many=True)
        return Response(serializer.data)