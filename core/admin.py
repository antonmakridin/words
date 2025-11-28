from django.contrib import admin
from .models import *

class MyWord(admin.ModelAdmin):
    list_display = ['slovo','perevod']

admin.site.register(Words, MyWord)
admin.site.register(Note)