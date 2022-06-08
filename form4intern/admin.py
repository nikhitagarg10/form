from django.contrib import admin
from .models.userdata import Userdata

class AdminUserdata(admin.ModelAdmin):
    list_display = ["fname", "lname", "Username", "email", "typee", "password", "city", "state", "pincode"]

# Register your models here.
admin.site.register(Userdata, AdminUserdata)