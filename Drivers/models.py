from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    role = models.CharField(max_length=30, choices=(("admin", "admin"), ("operator", "operator"), ("driver", "driver")))

class CarCategory(models.Model):
    minium = models.PositiveBigIntegerField()
    waiting_cost = models.PositiveBigIntegerField()
    bonus_percent = models.PositiveBigIntegerField()
    baggage_cost = models.PositiveBigIntegerField()
    type = models.CharField(max_length=30)
    sum_per_km = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Driver(CustomUser):
    last_name = None
    email = None
    first_name = None
    is_staff = None
    is_superuser = None
    fullname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    car_type = models.CharField(max_length=30)
    car_number = models.CharField(max_length=30)
    sms_code = models.CharField(max_length=30)
    confirmed = models.BooleanField(default=False)
    balance = models.PositiveBigIntegerField(default=0)
    gender = models.CharField(max_length=30, choices=(("man", "man"), ("woman", "woman")))
    has_baggage = models.BooleanField(default=False)
    created_at = models.DateField()
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    photo = models.FileField(null=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.fullname
