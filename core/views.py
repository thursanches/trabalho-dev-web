from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def studentLogin(request):
    return render(request, 'student-login.html')


def recruiterLogin(request):
    return render(request, 'recruiter-login.html')


def resetPassword(request):
    return render(request, 'reset-password.html')


def createAccountRecruiter(request):
    return render(request, 'create-account-recruiter.html')


def studentFirstAccess(request):
    return render(request, 'student-first-access.html')


def landingPageRecruiter(request):
    return render(request, 'landing-page-recruiter.html')


def curriculum(request):
    return render(request, 'curriculum.html')
