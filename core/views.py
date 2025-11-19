from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *

# Create your views here.
def main(request):
    return render(request, 'word/main.html')

def word (request):
    return render(request, 'word/word.html')