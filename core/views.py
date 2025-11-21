from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Words
from .forms import AddWord, AddNote
from django.contrib import messages

from .models import *

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = AddWord(request.POST)
        if form.is_valid():
            for field_name, field in form.cleaned_data.items():
                if isinstance(field, str):
                    form.cleaned_data[field_name] = field.lower()
            in_slovo = form.cleaned_data.get('slovo').lower()
            if Words.objects.filter(slovo=in_slovo,is_active=False).exists():
                form.add_error('slovo', 'Такое слово уже изучено.')
            elif Words.objects.filter(slovo=in_slovo,is_active=True).exists():
                form.add_error('slovo', 'Такое слово добавлено в список для изучения.')
            else:
                data = form.cleaned_data
                words = Words.objects.create(**data)
                return redirect('/')
    else:
        form = AddWord()

    words = Words.objects.all().filter(is_active=False)
    context = {
        'words': words,
        'form': form,
    }
    return render(request, 'word/main.html', context)

def word(request):
    if request.method == 'POST':
        form = AddNote(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            note = Note.objects.create(**data)
            return redirect('/word/')
    else:
        form = AddNote()
    notes = Note.objects.all()
    words = Words.objects.all().filter(is_active=True)
    context = {
        'words': words,
        'form': form,
        'notes': notes,
    }
    return render(request, 'word/word_success.html', context)

def show_word(request, word_id):
    words = Words.objects.get(id=word_id)
    context = {
        'words': words,
    }
    return render(request, 'word/word.html', context)

def delete_word(request, word_id):
    words = Words.objects.get(id=word_id)
    words.delete()
    return redirect('/')


def learn_word(request, word_id):
    word = get_object_or_404(Words, id=word_id)
    word.is_active = True
    word.save()
    messages.success(request, f'Слово "{word.slovo}" отмечено как изученное')
    return redirect('/')