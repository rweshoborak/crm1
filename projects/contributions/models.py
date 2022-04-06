from django.db import models

# Create your models here.
STATUS = (
    ('imeanza', 'started'),
    ('inaendelea', 'in_progres'),
    ('imeisha', 'Ended'),
)


class Source(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS)
    date_deposited = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Expenditure(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    status = models.CharField(max_length=25, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)


