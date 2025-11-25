from django import forms
from .models import *

class AddWord(forms.Form):
    slovo = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Слово'}),
        label='текст:'
        )
    perevod = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Перевод:'}),
        label='перевод:'
        )
    
    
class AddNote_old(forms.Form):
    note = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите заметку здесь...',
            'rows': 5
        }),
        label='заметка:'
    )

class AddNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']