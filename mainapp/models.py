from django.db import models


class User(models.Model):

    username = models.CharField(max_length=100)

    password = models.CharField(max_length=100)

    email = models.EmailField()


class Booking(models.Model):

    username = models.CharField(max_length=100)

    service = models.CharField(max_length=100)

    event_date = models.DateField()



class Recommendation(models.Model):

    username = models.CharField(max_length=100)

    service = models.CharField(max_length=100)

    predicted_price = models.FloatField()

    recommended_package = models.CharField(max_length=100)
