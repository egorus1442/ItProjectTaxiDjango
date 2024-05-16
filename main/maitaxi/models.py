from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    experience = models.DecimalField(decimal_places=1, max_digits=3)
    model_car = models.CharField(max_length=100)
    car_id = models.CharField(max_length=6)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    col_review = models.IntegerField()

    def __str__(self):
        return self.name


class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    departure_point = models.CharField(max_length=255)
    arrival_point = models.CharField(max_length=255)
    order_time = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)




