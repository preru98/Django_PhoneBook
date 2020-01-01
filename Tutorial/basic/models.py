from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_name=   models.CharField(max_length=200)
    contact_number= models.CharField(max_length=10)
    contact_email=  models.CharField(max_length=200)
    def __str__(self):
        detail=self.contact_name+' '+self.contact_number
        return detail
