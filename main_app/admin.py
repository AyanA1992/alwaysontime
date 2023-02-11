from django.contrib import admin

# Register your models here.
from .models import Salat, Prayers

# register
admin.site.register(Salat)
admin.site.register(Prayers)
