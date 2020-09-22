from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog9_app/home.html', {})

def about(request):
    return render(request, 'blog9_app/about.html', {})

def project(request):
    return render(request, 'blog9_app/project.html', {})

def services(request):
    return render(request, 'blog9_app/services.html', {})

def blog(request):
    return render(request, 'blog9_app/blog.html', {})

def pages(request):
    return render(request, 'blog9_app/pages.html', {})

def contact(request):
    return render(request, 'blog9_app/contact.html', {})