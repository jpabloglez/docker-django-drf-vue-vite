from django.db import models
import datetime

# Create your models here.
# References:
# * https://docs.djangoproject.com/en/4.0/topics/db/models/
# Each model is a Python class that subclasses django.db.models.Model.
class Analyses(models.Model):
    description = models.CharField(max_length=120)
    modality = models.CharField(max_length=60)
    status = models.CharField(max_length=20)
    customer = models.CharField(max_length=120)
    # duration = models.TimeField() # TODO automatic creation
    # created_at = models.DateTimeField(auto_now_add=True)# , default=datetime.datetime.now())
    # updated_at = models.DateTimeField(auto_now=True)# , default=datetime.datetime.now())

    # class Meta:
    #    ordering = ("-created_at",)

    def __str__(self):
        return self.description