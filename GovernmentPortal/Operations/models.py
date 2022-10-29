from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PublicUser(models.Model):
    user = models.OneToOneField(User,null = True, on_delete=models.CASCADE)
    EmploymentStatus = (
        ('Unemplyed', 'Unemplyed'),
        ('Employed', 'Employed'),
    )
    address = models.CharField(max_length=225, blank=True, null=True)
    email = models.EmailField(max_length=225)
    emplyment_status = models.CharField(max_length=225, blank=False, choices=EmploymentStatus)
    
    
class CabinetMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=225)
    role = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=225, blank=True, null=True)
    office_contact_number = models.IntegerField( null=True, blank=False)
    
    def __str__(self):
        return self.role
    
class Municipality(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)
    location = models.CharField(max_length= 100, blank=False, null=False)
    Head_officer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    contact_number = models.IntegerField( null=True, blank=False)
    
    def __str__(self):
        return self.name
    
class Government(models.Model):
    political_party = models.CharField(max_length = 200, blank=False, null=False)
    year_budget = models.CharField(max_length=100, blank=False, null=True)
    Municipality = models.ForeignKey(Municipality,null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.political_party
    
class PublicSector(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)
    year_budget = models.CharField(max_length=100, blank=True, null=True)
    head_minister = models.ForeignKey(CabinetMember, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)
    sector = models.ForeignKey(PublicSector, on_delete=models.CASCADE)
    budget = models.DecimalField(decimal_places = 2, max_digits=20)
    project_manager = models.CharField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return self.name
    