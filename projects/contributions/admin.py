from django.contrib import admin

from .models import *


# Register your models here.


class SourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'date_deposited']
    list_filter = ['amount', 'date_deposited']
    list_display_links = ['title']
    list_editable = ['amount']


admin.site.register(Source, SourceAdmin)


class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'descriptions', 'amount']
    list_filter = ['category', 'amount']
    list_display_links = ['title']
    list_editable = ['category', 'amount']


admin.site.register(Expenditure, ExpenditureAdmin)

admin.site.register(Category)
