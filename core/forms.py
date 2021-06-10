from django import forms
from django.forms import ModelForm
from localflavor.br.forms import BRZipCodeField


class resumeForm(forms.ModelForm):

    class Meta:
        model = resume
        fields = '__all__'
