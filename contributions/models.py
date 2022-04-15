from django.db import models


# Create your models here.

class Source(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    date_deposited = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Expenditure(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)
