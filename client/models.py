from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Client(models.Model,):
    
    First_Name = models.CharField(max_length=30)
    Middle_Initial = models.CharField(max_length=3)
    Last_Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50, unique=True)
    Phone_Number = PhoneNumberField(
        null=False, 
        blank=False, 
        unique=True
    )
    Comment = models.TextField(max_length=255, default='')
    Sub_Date = models.DateTimeField('Date Submitted', default='')
    Service = models.SlugField(
        max_length=25,
        unique=True,
        default=''
    )

    #class Meta:
     #   ordering = ('-name',)