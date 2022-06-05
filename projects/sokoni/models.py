from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Sokoni(models.Model):
    mtumiaji = models.OneToOneField(User,  on_delete=models.CASCADE)
    kitu = models.CharField(max_length=244, null=True)
    thamani = models.FloatField()
    idadi = models.IntegerField()

    def __str__(self):
        return self.kitu


class Ujenzi(models.Model):
    mtumiaji = models.OneToOneField(User, on_delete=models.CASCADE)
    kitu = models.CharField(max_length=244, null=True)
    thamani = models.FloatField()
    idadi = models.IntegerField()

    def  __str__(self):
        return self.kitu


class Mifugo(models.Model):
    name = models.CharField(max_length=244)
    DOB = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name




