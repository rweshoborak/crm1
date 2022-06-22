from django.db import models


# Create your models here.

class Source(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    date_deposited = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ItemCategory(models.Model):
    category = models.CharField(max_length=255, default="Home")

    def __str__(self):
        return self.category


class Expenditure(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    quantity = models.FloatField()
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)


class Ternants(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Rent(models.Model):
    ternant = models.OneToOneField(Ternants,on_delete=models.CASCADE)
    house_no = models.CharField(max_length=56)
    location = models.CharField(max_length=56)
    rent_amount = models.FloatField()
    months = models.IntegerField()
    Due_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ternant , self.rent_amount








