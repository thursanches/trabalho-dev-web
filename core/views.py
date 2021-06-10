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

    resume = {
        'curriculum': {
            'name': 'Juan Pablor',
            'age': '20 anos',
            'skills': 'JS, React, Django',
            'city': 'Ibirité',
            'description': 'O brabor de ibirité, DJ Azeitona'
        }
    }

    data = {
        'resume_items': resume
    }
    return render(request, 'landing-page.html', data)


def resume(request):
    return render(request, 'resume.html')
