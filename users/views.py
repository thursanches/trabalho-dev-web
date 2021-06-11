from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def createAccount(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        email_confirmation = request.POST['email_confirmation']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if not name.strip():
            print('O nome não pode ficar em branco')
            return redirect('create-account')

        if not email.strip():
            print('O email não pode ficar em branco')
            return redirect('create-account')

        if email != email_confirmation:
            print('As senhas não são iguais')
            return redirect('create-account')

        if password != password_confirmation:
            print('As senhas não são iguais')
            return redirect('create-account')

        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('create-account')

        user = User.objects.create_user(
            username=name, email=email, password=password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'users/create-account.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email == "" or password == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, password)

        if User.objects.filter(email=email).exists():
            name = User.objects.filter(
                email=email).values_list('username', flat=True).get()
            user = auth.authenticate(
                request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('landing-page')
    return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def resetPassword(request):
    pass


def studentFirstAccess(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/student-first-access')
    else:
        return redirect('index')
