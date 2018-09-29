from django.db import models

# Create your models here.
class Musk(models.Model):
	Id = models.IntegerField(primary_key=True)
	Date = models.DateTimeField()
	Address = models.TextField(max_length=500)
	Species = models.CharField(max_length=100)
	Block = models.IntegerField()
	Street = models.CharField(max_length = 200)
	Trap = models.CharField(max_length=200)
	AddressNumberAndStreet = models.CharField(max_length=200)
	Latitude = models.DecimalField(max_digits=20, decimal_places=20)
	Longitude = models.DecimalField(max_digits=20, decimal_places=20)
	AddressAccuracy = models.IntegerField()


