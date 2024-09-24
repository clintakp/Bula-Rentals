from django.db import models

# Create your models here.

class Vehicles(models.Model):
    id = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('rented', 'Rented'), ('maintenance', 'Maintenance')], default='available')
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    seating_capacity = models.IntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)
    size = models.CharField(max_length=20)
    classes = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        managed = False  
        db_table = 'vehicles'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    question = models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
