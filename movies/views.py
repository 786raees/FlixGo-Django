from django.shortcuts import render

def error_404(request):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def catalog(request):
    return render(request, 'catalog.html')

def contacts(request):
    return render(request, 'contacts.html')

def details(request):
    return render(request, 'details.html')

def forgot_password(request):
    return render(request, 'forgot.html')

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')
