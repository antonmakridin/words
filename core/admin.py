from django.contrib import admin
from .models import *

class MyWord(admin.ModelAdmin):
    list_display = ['slovo','perevod']


class MyLikesCounter(admin.ModelAdmin):
    list_display = ['name','slug','likes']

admin.site.register(Words, MyWord)
admin.site.register(Note)
admin.site.register(LikesCounter, MyLikesCounter)
