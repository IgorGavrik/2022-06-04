from django.urls import path
from . import views
from .views import Login, RegistrationView

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('post', views.post, name='post'),
    path('article_detail/<slug:slug>/', views.post_detail, name='post_detail'),
]
