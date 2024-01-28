from rest_framework.serializers import ModelSerializer
from .models import *

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class OperatorSerializer(ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__al__'