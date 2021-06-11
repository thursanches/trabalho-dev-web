from django.urls import path

from users.views import login, resetPassword, createAccount, studentFirstAccess, logout

urlpatterns = [
    path('create-account/', createAccount,
         name='create-account'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('reset-password/', resetPassword, name='reset-password'),
    path('student-first-access/', studentFirstAccess,
         name='student-first-access'),
]
