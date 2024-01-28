from django.db import models
from Drivers.models import CustomUser, Driver

# Create your models here.
class Client(models.Model):
    phone = models.CharField(max_length=30)
    total_bonus = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.phone

class Operator(CustomUser):
    ish_vaqti = models.CharField(max_length=30)
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)

    def __str__(self):
        return self.ism

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    total_sum = models.PositiveBigIntegerField(default=0)
    baggage = models.BooleanField(default=False)
    for_women = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=(('active', 'active'), ('olindi', 'olindi'), ('boshlandi', 'boshlandi'), ('tugadi', 'tugadi'), ('bekor qilindi', 'bekor qilindi')))
    starting_point = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    grading_point = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    waiting_seconds = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.driver.fullname