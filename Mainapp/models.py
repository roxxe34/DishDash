from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# MODELS DATABASES : CUSTOMER
class Customer(models.Model):
    name = models.CharField('Nom', max_length=50, null=True)
    phone = models.CharField('Téléphone', max_length=10, null=True)
    email = models.EmailField('Email', null=True)
    created_date = models.DateTimeField('Date de création', auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# MODELS DATABASES :  USER
class Profile(AbstractBaseUser,PermissionsMixin):
    first_name =models.CharField(max_length=250)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    mobile =models.CharField('Téléphone',max_length=10)
    status = models.BooleanField(default=True)
    designation = models.CharField('désignation',max_length=50, null=True)
    salary = models.CharField('salaire',max_length=50, null=True)
    number_of_projects = models.IntegerField('nombre_de_projets', null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

# MODELS DATABASES : PROJECT
class Project(models.Model):
    title = models.CharField('titre', max_length=50, null=True)
    description = models.TextField()
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,verbose_name='client')
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,verbose_name='profil')

    def __str__(self):
        return self.title

# MODELS DATABASES : TASK
class Task(models.Model):
    title = models.CharField('titre', max_length=50, null=True)
    description = models.TextField()
    cost_per_houre = models.FloatField('coût par heure', null=True)
    duration = models.IntegerField('durée', null=True)
    total_cost = models.IntegerField('coût total', null=True)
    
    def __str__(self):
        return self.title

# MODELS DATABASES : INVOICE
class Invoice(models.Model):
    invoice_number = models.CharField('Numéro de facture', max_length=50, null=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    invoice_details = models.TextField('Détails de la facture', null=True)
    project_duration = models.IntegerField('durée', null=True)
    total_cost = models.FloatField('coût total', null=True)
    note = models.TextField('Remarque', null=True)
    
    def __str__(self):
        return self.title