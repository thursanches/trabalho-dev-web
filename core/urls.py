from django.urls import path
from .views import index, studentFirstAccess, studentLogin, curriculum, landingPageRecruiter, recruiterLogin, resetPassword, createAccountRecruiter

urlpatterns = [
    path('', index, name='index'),
    path('student-login/', studentLogin, name='student-login'),
    path('recruiter-login/', recruiterLogin, name='recruiter-login'),
    path('student-first-access/', studentFirstAccess,
         name='student-first-access'),
    path('create-account-recruiter/', createAccountRecruiter,
         name='create-account-recruiter'),
    path('reset-password/', resetPassword, name='reset-password'),
    path('landing-page-recruiter/', landingPageRecruiter,
         name='landing-page-recruiter'),
    path('curriculum/', curriculum, name='curriculum')
]
