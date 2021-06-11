from django.urls import path
from .views import index, resume, landingPage,  search

urlpatterns = [
    path('', index, name='index'),
    path('landing-page/', landingPage,
         name='landing-page'),
    path('<int:resume_id>', resume, name='resume'),
    path('search', search, name='search')
]
