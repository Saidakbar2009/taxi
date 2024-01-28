from rest_framework.serializers import ModelSerializer
from .models import *

class CarCategorySerializer(ModelSerializer):
    class Meta:
        model = CarCategory
        fields = '__all__'

class DriverSerialzer(ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'