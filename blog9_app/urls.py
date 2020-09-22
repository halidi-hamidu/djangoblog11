from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home', views.home, name='home'),
    path('About', views.about, name='About'),
    path('project', views.project, name='project'),
    path('services', views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('pages', views.pages, name='pages'),
    path('contact', views.contact, name='contact'),


]