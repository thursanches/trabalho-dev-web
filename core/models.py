from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRPostalCodeField, BRStateField
from localflavor.br.br_states import STATE_CHOICES


class resume(models.Model):

    class civilState(models.TextChoices):
        SINGLE = 'Solteiro(a)', _('Solteiro(a)')
        MARRIED = 'Casado', _('Casado(a)')
        DIVORCED = 'Divorciado(a)', _('Divorciado(a)')
        WIDOW = 'Viúvo(a)', _('Viúvo(a)')

    def is_upperclass(self):
        return self.civil_state in {
            self.civilState.DIVORCED,
            self.civilState.SINGLE,
        }

    class genderChoices(models.TextChoices):
        MALE = 'Masculino', _('Masculino')
        FEMALE = 'Feminino', _('Feminino')
        OTHER = 'Outro', _('Outro')

    class deficiency(models.TextChoices):
        YES = 'Sim', _('Sim')
        NO = 'Não', _('Não')

    class scholarshipLevel(models.TextChoices):
        FUNDAMENTAL_INCOMPLETE = 'Ensino Fundamental Incompleto', _(
            'Ensino Fundamental Completo')
        FUNDAMENTAL_COMPLETE = 'Ensino Fundamental Completo', _(
            'Ensino Fundamental Incompleto')
        HIGHSCHOOL_INCOMPLETE = 'Ensino Médio Incompleto', _(
            'Ensino Médio Incompleto')
        HIGHSCHOOL_COMPLETE = 'Ensino Médio Completo', _(
            'Ensino Médio Completo')
        COLLEGE_INCOMPLETE = 'Ensino Superior Incompleto', _(
            'Ensino Superior Incompleto')
        COLLEGE_COMPLETE = 'Ensino Superior Completo', _(
            'Ensino Superior Completo')

    class formation(models.TextChoices):
        BACHELOR = 'Bacharelado', _('Bacharelado')
        GRADUATION = 'Licenciatura', _('Licenciatura')
        TECHNOLOGIST = 'Tecnólogo', _('Tecnólogo')
        SPECIALIZATION = 'Especialização', _('Especialização')
        MBA = 'MBA', _('MBA')
        MASTERS_DEGREE = 'Mestrado', _('Mestrado')
        DOCTORATE_DEGREE = 'Doutorado', _('Doutorado')
        POST_DOCTORAL = 'Pós-Doutorado', _('Pós-Doutorado')

    resume_id = models.AutoField(primary_key=True)

    # Profile Image
    # Necessário configura o Media Root
    profile_image = models.ImageField(blank="true")

    # Informações pessoais
    name = models.CharField(max_length=200)
    birthday = models.DateField()

    civil_state = models.CharField(
        max_length=13, choices=civilState.choices, default=civilState.SINGLE)
    nationality = models.CharField(max_length=50)

    gender = models.CharField(choices=genderChoices.choices, max_length=9)

    # Endereço

    postal_code = BRPostalCodeField(max_length=9)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    # Contatos

    email = models.EmailField()
    telephone = models.CharField(max_length=(14))
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    other_social_media = models.URLField(blank=True)

    # Sobre mim
    description = models.TextField(max_length=500)

    # Pessoa com Deficiência
    deficient_person = models.CharField(
        choices=deficiency.choices, max_length=3)
    if_deficient = models.CharField(max_length=100, blank=True)

    # Formação Acadêmica
    scholarship_level = models.CharField(
        choices=scholarshipLevel.choices, max_length=50, blank=True)

    formation_kind = models.CharField(
        choices=formation.choices, max_length=50, blank=True)
    education_institution = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(blank=True)
    finish_date = models.DateField(blank=True)

    # Objetivos Profissionais
    professional_objectives = models.TextField(max_length=500)

    # Skills

    skills = models.TextField(max_length=500)

    # Experiência Profissional
    company = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=30, blank=True)
    professional_area = models.CharField(max_length=30, blank=True)
    salary = models.DecimalField(
        decimal_places=2, max_digits=99999999, blank=True)
    start_company_date = models.DateField(blank=True)
    finish_company_date = models.DateField(blank=True)
    function_role = models.TextField(max_length=500, blank=True)

    # Certificações
    certifications = models.TextField(max_length=500, blank=True)

    # Idiomas
    languages = models.TextField(max_length=500, blank=True)

    # Data de publicação
    published_time = models.DateTimeField(default=datetime.now, blank=True)
