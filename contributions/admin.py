from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register([Source, Expenditure,ItemCategory,Rent,Ternants])
