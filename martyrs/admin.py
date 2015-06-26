from django.contrib import admin
from .models import Martyr

class MartyrAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_death', 'governorate')

admin.site.register(Martyr, MartyrAdmin)
