from django.db import models

# Create your models here.

class data (models.Model):
    un=models.CharField(max_length=100)
    pw=models.CharField(max_length=100)

    def __str__(self):
        return self.un
