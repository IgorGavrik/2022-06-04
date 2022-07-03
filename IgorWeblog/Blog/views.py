from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    tasks = Task.objects.all().order_by('-id')
    if 'page' in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    paginator = Paginator(tasks, 3)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Блог главная', 'tasks': tasks, 'page_obj': page_obj, 'page_number': page_number, 'page': page}
    return render(request, 'Blog/index.html', context)


class RegistrationView(View, UserCreationForm):
    def get(self, request):
        if request.user:
            return render(request, 'Blog/registration.html')
        else:
            return redirect('/')

    def post(self, request):
        data = dict(request.POST)
        if data.get('password') == data.get('re_password'):
            user = User.objects.create(
                username=data.get('email'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                password=data.get('password'),
            )
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'Blog/registration.html', {'re_password': "Не совпадают"})


class Login(LoginView):
    success_url = reverse_lazy('index')
    success_msg = 'Вы авторизованы'

    def get(self, request):
        if request.user:
            return render(request, 'Blog/login.html')
        else:
            return redirect('/')

    def post(self, request):
        user = authenticate(
            username=User.objects.get(email=request.POST.get('email')).username,
            password=request.POST.get('password')
        )
        print(user)
        print(request.POST)
        if user:
            login(request, user)
            return redirect('/')
        return render(request, 'Blog/login.html', {"error": "Что-то не так"})


class Logout(LogoutView):
    def get(self, request):
        if request.user:
            return render(request, 'Blog/logout.html')
        else:
            return redirect('/')


def post(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {'form': form, 'error': error}
    return render(request, 'Blog/post.html', context)


def post_detail(request, post, slug):
    post == get_object_or_404(Task, slug=post_detail())
    return render(request, 'Blog/article_detail.html', {'slug': slug})
