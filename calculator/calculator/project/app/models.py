from django.db import models

# Create your models here.

class Calculator(models.Model):
    c_id = models.AutoField(primary_key=True, unique = True)
    c_first=models.CharField(max_length=1000,default="")
    c_second=models.CharField(max_length=1000,default="")
    c_operator=models.CharField(max_length=4,default="")
    c_result=models.CharField(max_length=10000,default="")
    

