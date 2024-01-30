from django.urls import path
from .views import *

urlpatterns = [
    path('token_olish_operator/', OperatorTokenApiView.as_view()),
    path('token_olish_driver/', DriverTokenApiView.as_view()),
    path('drivers/', DriversApiView.as_view()),
    path('driver/<int:pk>', DriverApiView.as_view()),
    path('category/', CarCategoryApiView.as_view())
]