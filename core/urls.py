from django.urls import path
from .views import index, studentFirstAccess, resume, landingPage, login, resetPassword, createAccount, search

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('student-first-access/', studentFirstAccess,
         name='student-first-access'),
    path('create-account/', createAccount,
         name='create-account'),
    path('reset-password/', resetPassword, name='reset-password'),
    path('landing-page/', landingPage,
         name='landing-page'),
    path('<int:resume_id>', resume, name='resume'),
    path('search', search, name='search')
]
