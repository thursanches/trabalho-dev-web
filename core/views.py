from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def resetPassword(request):
    return render(request, 'reset-password.html')


def createAccount(request):
    return render(request, 'create-account.html')


def studentFirstAccess(request):
    return render(request, 'student-first-access.html')


def landingPage(request):
    return render(request, 'landing-page.html')


def resume(request):
    return render(request, 'resume.html')
