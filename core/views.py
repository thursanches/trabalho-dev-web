from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Resume
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def landingPage(request):

    resume = Resume.objects.order_by('-published_time').all()

    data = {
        'resumes': resume
    }
    return render(request, 'landing-page.html', data)


def resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    resume_to_expose = {
        'resume': resume
    }
    return render(request, 'resume.html', resume_to_expose)


def search(request):
    list_resume = Resume.objects.order_by('-published_time').all()

    if 'search' in request.GET:
        resume_to_search = request.GET['search']
        if resume_to_search:
            list_resume = list_resume.filter(Q(
                skills__icontains=resume_to_search)
                | Q(name__icontains=resume_to_search)
                | Q(course__icontains=resume_to_search)
                | Q(certifications__icontains=resume_to_search)
                | Q(city__icontains=resume_to_search)
                | Q(state__icontains=resume_to_search)
                | Q(scholarship_level__icontains=resume_to_search)
                | Q(professional_area__icontains=resume_to_search)
                | Q(role__icontains=resume_to_search)
            )

    data = {
        'resumes': list_resume
    }

    return render(request, 'search.html', data)
