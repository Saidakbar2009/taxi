from django.urls import path
from .views import *

urlpatterns = [
    path('order_create/', OrderCreateApiView.as_view())
]