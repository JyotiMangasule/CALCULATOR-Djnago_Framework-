from django.db import models

# Create your models here.



class Calculations(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operation = models.CharField(max_length=10)
    result = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    

