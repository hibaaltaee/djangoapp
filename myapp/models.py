from django.db import models

# Create your models here.
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', default='default.jpg')

    def __str__(self):
        return self.name



# myapp/models.py

# myapp/models.py


from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    occasion = models.CharField(max_length=50, blank=True, null=True)
    guests = models.PositiveIntegerField(default=1)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.date_time}"
