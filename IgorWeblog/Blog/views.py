from django.shortcuts import render, redirect
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


def registration(request):
    return render(request, 'Blog/registration.html')


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