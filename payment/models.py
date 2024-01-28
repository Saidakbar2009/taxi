from django.db import models
from Drivers.models import Driver
from operators.models import Operator
# Create your models here.
class Payment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    type = models.CharField(max_length=30, choices=(('naxt', 'naxt'), ('karta', 'karta')))
    date = models.DateField()
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)

    def __str__(self):
        return self.operator.ism