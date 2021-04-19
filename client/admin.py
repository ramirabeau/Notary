from django.contrib import admin
from .models import Client, Service

#admin.site.register(Client)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("Last_Name", "First_Name")

""" @admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("poa", "docs", "wills")
 """
# Register your models here.
