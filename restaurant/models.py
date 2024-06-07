from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField(verbose_name='Date (yyyy-mm-dd)')
    time = models.TimeField(verbose_name='Time (hh:mm)')

    def __str__(self):
        return f'{self.name}'
        

class Menu(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    description = models.TextField(1000, default= '')

    def __str__(self):
        return self.name
                                 