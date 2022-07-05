from django import forms
from .models import Task, Comment
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите заголовок"
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст поста'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ваше имя"
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес электронной почты'
            }),
            "body": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите коментарий'
            })
        }
