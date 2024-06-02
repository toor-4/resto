from django.db import models

# Create your models here.
class Booking(models.Model):
    firs_name = models.CharField(max_length = 200 )
    last_name = models.CharField(max_length = 200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        

class Menu(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    description = models.TextField(1000, default= '')

    def __str__(self):
        return self.name
                                 