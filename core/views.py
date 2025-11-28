from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Words
from .forms import AddWord, AddNote
from django.contrib import messages

from .models import *

def raz(num):
    numbers = {
    '1': 'раз',
    '2': 'раза',
    '3': 'раза',
    '4': 'раза',
    '5': 'раз',
    '6': 'раз',
    '7': 'раз',
    '8': 'раз',
    '9': 'раз',
    '0': 'раз'
    }
    for key, value in numbers.items():
        if key == num:
            return(value)

# Create your views here.
def main(request):
    status = request.GET.get('status')
    if status:
        words = Words.objects.all().filter(is_active=status)
    else:
        words = Words.objects.all().filter(is_active=False)
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    razn = raz(str(num_visits)[-1])
    request.session['num_visits'] = num_visits+1

    if request.method == 'POST':
        form = AddWord(request.POST)
        if form.is_valid():
            for field_name, field in form.cleaned_data.items():
                if isinstance(field, str):
                    form.cleaned_data[field_name] = field.lower()
            data = form.cleaned_data
            words = Words.objects.create(**data)
            return redirect('/')
    else:
        form = AddWord()
    
    if request.method == 'POST':
        formNote = AddNote(request.POST)
        if formNote.is_valid():
            data = formNote.cleaned_data
            note = Note.objects.create(**data)
            return redirect('/?status=1')
    else:
        formNote = AddNote()
    notes = Note.objects.all()
    context = {
        'words': words,
        'form': form,
        'num_visits':num_visits,
        'razn' : razn,
        'status': status,
    }
    return render(request, 'word/main.html', context)

def word(request):
    
    words = Words.objects.all().filter(is_active=True)
    context = {
        'words': words,
    }
    return render(request, 'word/word_success.html', context)

def show_word(request, word_id):
    word = Words.objects.get(id=word_id)
    notes = Note.objects.filter(word_id=word_id)
    
    if request.method == 'POST':
        formNote = AddNote(request.POST)
        if formNote.is_valid():
            note = formNote.save(commit=False)
            note.word = word
            note.save()
            return redirect('show_word', word_id)
    else:
        formNote = AddNote()
        
    context = {
        'word': word,
        'notes': notes,
        'formNote': formNote,
    }
    return render(request, 'word/word.html', context)
        

def delete_word(request, word_id):
    words = Words.objects.get(id=word_id)
    words.delete()
    return redirect('/')


def learn_word(request, word_id):
    word = get_object_or_404(Words, id=word_id)
    if word.is_active == True:
        word.is_active = False
    else:
        word.is_active = True
    word.save()
    return redirect('show_word', word_id)
