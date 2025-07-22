from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    print("SI ENTRA Aquí")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("SI loguea")
            return redirect('menu')  # Cambia a la ruta principal de tu app
        else:
            print('Usuario o contraseña incorrectos.')
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'home/index.html')
