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
        fields = '__all__'

    extra_kwargs = {
        "driver": {'read_only': True},
        'status': {'read_only': True},
        'grade': {'read_only': True},
        'waiting_second': {'read_only': True},
        'total_sum': {'read_only': True}
    }