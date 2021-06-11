from django.contrib import admin
from .models import Resume


class ListingResumes(admin.ModelAdmin):
    list_display = ('resume_id', 'name', 'email', 'published_time')
    list_display_links = ('resume_id', 'name', 'email')
    search_fields = ('skills', 'course', 'description', 'role',
                     'professional_objectives', 'professional_area', 'certifications', 'languages', 'scholarship_level', 'city', 'district', 'state', 'name', 'resume_id')
    list_filter = ('published_time',)
    list_per_page = 20


admin.site.register(Resume, ListingResumes)
