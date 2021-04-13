from django.contrib import admin
from .models import Client

#admin.site.register(Client)

@admin.register(Client)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("Last_Name", "First_Name")

# Register your models here.
