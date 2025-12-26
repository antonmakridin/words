import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Words, LikesCounter
from .forms import AddWord, AddNote
from django.contrib import messages
from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

    if request.method == 'POST' and request.user.is_authenticated:
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

    likes_count = LikesCounter.objects.get(slug="main")

    context = {
        'words': words,
        'form': form,
        'num_visits':num_visits,
        'razn' : razn,
        'status': status,
        'likes_count': likes_count,
    }
    return render(request, 'word/main.html', context)

@login_required
def word(request, word_id):

    profile = request.user.profile
    words = Words.objects.all().filter(is_active=True)

    if profile.id != words.profile.id:
        raise Http404

    context = {
        'words': words,
    }
    return render(request, 'word/word_success.html', context)

def show_word(request, word_id):
    word = Words.objects.get(id=word_id)
    # notes = Note.objects.filter(word_id=word_id)
    # эквивалент
    notes = word.zametki.all()
    
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



class HelloView(View):

    def get_words(self):
        word = Words.objects.all()
        return word

    def get(self, request):
        word = self.get_words
        context = {'words': word}
        return render(request, 'class.html', context)
    
    def post(self, request):
        pass
    

class MyTemplateView(TemplateView):
    template_name = 'class.html'

    def get_context_data(self, **kwargs):
        return {'words': 'slovechko'}
    
def testjs(request):
    print('Новый запрос')
    return render(request, 'testjs.html' )

def get_data(request):

    return JsonResponse({'text': 'привет'})

@csrf_exempt
def thx_data(request):

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name_slug = data.get('slug')
        if not name_slug:
            return JsonResponse({'error': 'No slug provided'}, status=400)

        try:
            likes_counter = LikesCounter.objects.get(slug=name_slug)
            likes_counter.likes += 1
            likes_counter.save()
            return JsonResponse({'likes_count': likes_counter.likes})
        except LikesCounter.DoesNotExist:
            return JsonResponse({'error': 'Invalid slug'}, status=400)