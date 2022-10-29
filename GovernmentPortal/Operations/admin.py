from django.contrib import admin
from . models import CabinetMember, Project, PublicSector, PublicUser,Municipality, Government,PublicSector
# Register your models here.

@admin.register(CabinetMember)
class CabinetMemberAdmin(admin.ModelAdmin):
    fields = ('user', 'email', 'role','address','office_contact_number')
    list_display = ('user', 'email', 'role','address','office_contact_number')
    ordering = ('role',)

@admin.register(PublicUser)
class PublicUserAdmin(admin.ModelAdmin):
    fields = ('user','email', 'address','emplyment_status')
    list_display = ('user','email', 'address','emplyment_status')
    ordering = ('email',)

@admin.register(PublicSector)
class PublicSectorAdmin(admin.ModelAdmin):
    fields = ('name', 'year_budget', 'Head_minister')
    list_display = ('name', 'year_budget')
    ordering = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'sector', 'budget','project_manager')
    list_display = ('name', 'sector', 'budget','project_manager')
    ordering = ('name',)

@admin.register(Government)
class GovernmentAdmin(admin.ModelAdmin):
    fields = ('political_party', 'year_budget', 'municipality')
    list_display = ('political_party', 'year_budget',)
    ordering = ('political_party',)

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'head_officer','contact_number')
    list_display = ('name', 'location','contact_number')
    ordering = ('name',)

