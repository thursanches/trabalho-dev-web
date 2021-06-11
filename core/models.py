from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRPostalCodeField, BRStateField


class Resume(models.Model):

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

    resume_id = models.AutoField("ID do Currículo", primary_key=True)

    # Profile Image
    # Necessário configura o Media Root
    profile_image = models.ImageField(
        "Imagem de Perfil", upload_to='pictures/%d/%m/%Y/', blank="true",)

    # Informações pessoais
    name = models.CharField("Nome Completo", max_length=200)
    birthday = models.DateField("Data de Nascimento")

    civil_state = models.CharField("Estado Civil",
                                   max_length=13, choices=civilState.choices, default=civilState.SINGLE)
    nationality = models.CharField("Nacionalidade", max_length=50)

    gender = models.CharField(
        "Gênero", choices=genderChoices.choices, max_length=9)

    # Endereço

    postal_code = BRPostalCodeField("CEP", max_length=9)
    street = models.CharField("Logradouro", max_length=100)
    district = models.CharField("Bairro", max_length=100)
    city = models.CharField("Cidade", max_length=100)
    state = BRStateField("Estado", max_length=50)

    # Contatos

    email = models.EmailField("E-mail")
    telephone = models.CharField("Telefone", max_length=(14))
    linkedin = models.URLField("Linkedin", blank=True)
    facebook = models.URLField("Facebook", blank=True)
    instagram = models.URLField("Instagram", blank=True)
    other_social_media = models.URLField("Outra mídia social", blank=True)

    # Sobre mim
    description = models.TextField("Descrição", max_length=500)

    # Pessoa com Deficiência
    deficient_person = models.CharField("Pessoa com deficiência?",
                                        choices=deficiency.choices, max_length=3)
    if_deficient = models.CharField(
        "Se sim, descreva a deficiência", max_length=100, blank=True)

    # Formação Acadêmica
    scholarship_level = models.CharField("Nível de escolaridade",
                                         choices=scholarshipLevel.choices, max_length=50, blank=True)

    formation_kind = models.CharField("Tipo de formação",
                                      choices=formation.choices, max_length=50, blank=True)
    education_institution = models.CharField(
        "Instituição de Ensino", max_length=100, blank=True)
    course = models.CharField("Curso", max_length=50, blank=True)
    start_date = models.DateField("Data de Início", blank=True)
    finish_date = models.DateField("Data de finalização", blank=True)

    # Objetivos Profissionais
    professional_objectives = models.TextField(
        "Objetivos profissionais", max_length=500)

    # Skills

    skills = models.TextField("Habilidades", max_length=500)

    # Experiência Profissional
    company = models.CharField("Empresa", max_length=50, blank=True)
    role = models.CharField("Cargo", max_length=30, blank=True)
    professional_area = models.CharField(
        "Área profissional", max_length=30, blank=True)
    salary = models.DecimalField("Salário",
                                 decimal_places=2, max_digits=99999999, blank=True)
    start_company_date = models.DateField("Data de início", blank=True)
    finish_company_date = models.DateField(
        "Data do Fim (se houver)", blank=True)
    function_role = models.TextField(
        "Descreva as funções", max_length=500, blank=True)

    # Certificações
    certifications = models.TextField(
        "Certificações", max_length=500, blank=True)

    # Idiomas
    languages = models.TextField("Linguagens", max_length=500, blank=True)

    # Data de publicação
    published_time = models.DateTimeField(
        "Publicado em: ", default=datetime.now, blank=True)

    def __str__(self):
        return self.name
