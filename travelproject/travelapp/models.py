from django.db import models

# Create your models here.


class Contact(models.Model):
    usn = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    sem = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __self__(self):
        return self.name
