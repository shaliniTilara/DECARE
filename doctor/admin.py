from django.contrib import admin
from .models import Client,Doctor
from django.contrib import admin
#from .models import Doctor, Patient
# Register your models here.
admin.site.register(Client)
admin.site.register(Doctor)

class Clientadmin(admin.ModelAdmin):
    list_display=["id","name","email","phone","disease","city","msg"]

    
class Doctoradmin(admin.ModelAdmin):
    list_display=["name","specialization","email","phone"]

    
