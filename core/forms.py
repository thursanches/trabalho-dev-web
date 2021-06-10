from django import forms
from django.forms import ModelForm
from core.models import resume
from localflavor.br.forms import BRZipCodeField


class resumeForm(forms.ModelForm):

    class Meta:
        model = resume
        exclude = ['published_time']
        localized_fields = '__all__'
