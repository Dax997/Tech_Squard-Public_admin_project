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
    emplyment_status = models.CharField(max_length=225, blank=False, choices=EmploymentStatus)

    def __str__(self):
        return self.user.username
class CabinetPosition(models.Model):
    position = models.CharField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return self.position    
    
class CabinetMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.OneToOneField(CabinetPosition, blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=225, blank=True, null=True)
    office_contact_number = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return self.role.position
    
class Municipality(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)
    location = models.CharField(max_length= 100, blank=False, null=False)
    head_officer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return self.name


class PublicSector(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)
    year_budget = models.CharField(max_length=100, blank=True, null=True)
    head_minister = models.ForeignKey(CabinetMember, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
class BudgetAllocation(models.Model):
    public_sector = models.ForeignKey(PublicSector, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=225, blank=False, null=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.purpose
  

class PromissedDuty(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)
    sector = models.ForeignKey(PublicSector, max_length=225, null=False, blank=False, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000, blank=False, null=False)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Government(models.Model):
    political_party = models.CharField(max_length = 200, blank=False, null=False)
    total_budget = models.CharField(max_length=100, blank=False, null=True)
    promissed_duties = models.ForeignKey(PromissedDuty, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.political_party
  

class Project(models.Model):
    Project_status = (
        ('Complete', 'Complete'),
        ('Not Complete', 'Not Complete'),
        ('Half Complete', 'Half Complete'),
    )
    
  
    name = models.CharField(max_length=225, blank=False, null=False)
    sector = models.ForeignKey(PublicSector, on_delete=models.CASCADE)
    budget = models.DecimalField(decimal_places = 2, max_digits=20)
    project_manager = models.ForeignKey(PublicUser, on_delete=models.CASCADE)
    project_status = models.CharField(max_length=225,choices=Project_status, default='Not Complete')

    
    def __str__(self):
        return self.name
    
class PublicComment(models.Model):
    user = models.ForeignKey(PublicUser,null=True, blank=False, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=225, blank=False, null=False)
    project = models.ForeignKey(Project, null=True ,blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.user.username
