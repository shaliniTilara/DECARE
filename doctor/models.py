from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=20)
    adharno = models.IntegerField(null=True, blank=True)
    email=models.EmailField()
    phone=models.IntegerField()
    DISEASE_CHOICES = [
        ('flu', 'Flu'),
        ('covid', 'COVID-19'),
        ('diabetes', 'Diabetes'),
        ('bp', 'Blood Pressure'),
        ('other', 'Other'),
    ]
    disease = models.CharField(max_length=20, choices=DISEASE_CHOICES)

    CITY_CHOICES = [
        ('delhi', 'Delhi'),
        ('mumbai', 'Mumbai'),
        ('bangalore', 'Bangalore'),
        ('chennai', 'Chennai'),
        ('other', 'Other'),
    ]
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    

    def __str__(self):
        return self.name
    

    

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

