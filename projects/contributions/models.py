from django.db import models
from django.utils.safestring import mark_safe
from tinymce import models as tinymce_models


# Create your models here.

class Source(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    date_deposited = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    cat_name = models.CharField(max_length=50, null=True, default='Home')

    def __str__(self):
        return self.cat_name


class Expenditure(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    description = tinymce_models.HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

    def descriptions(self):
        return mark_safe(self.description)
