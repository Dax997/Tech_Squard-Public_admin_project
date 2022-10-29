from django.contrib import admin
from . models import BudgetAllocation,PromissedDuty, CabinetMember, CabinetPosition, Project, PublicSector, PublicUser,Municipality, Government,PublicSector
# Register your models here.

@admin.register(PromissedDuty)
class PromissedDutyAdmin(admin.ModelAdmin):
    fields = ('name','sector','message','complete')
    list_display = ('name','sector','message', 'complete')
    ordering = ('name',)
@admin.register(BudgetAllocation)
class BudgetAllocationAdmin(admin.ModelAdmin):
    fields = ('public_sector','purpose','amount')
    list_display = ('purpose','amount','public_sector')
    ordering = ('amount',)
    
@admin.register(CabinetPosition)
class CabinetPositionAdmin(admin.ModelAdmin):
    fields = ('position',)
    list_display = ('position',)
    ordering = ('position',)
@admin.register(CabinetMember)
class CabinetMemberAdmin(admin.ModelAdmin):
    fields = ('user', 'role','address','office_contact_number')
    list_display = ('user', 'role','address','office_contact_number')
    ordering = ('role',)

@admin.register(PublicUser)
class PublicUserAdmin(admin.ModelAdmin):
    fields = ('user', 'address','emplyment_status')
    list_display = ('user', 'address','emplyment_status')
    ordering = ('address',)

@admin.register(PublicSector)
class PublicSectorAdmin(admin.ModelAdmin):
    fields = ('name', 'year_budget', 'head_minister')
    list_display = ('name', 'year_budget')
    ordering = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'sector', 'budget','project_manager')
    list_display = ('name', 'sector', 'budget','project_manager')
    ordering = ('name',)

@admin.register(Government)
class GovernmentAdmin(admin.ModelAdmin):
    fields = ('political_party', 'total_budget', 'promissed_duties')
    list_display = ('political_party', 'total_budget')
    ordering = ('political_party',)

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'head_officer','contact_number')
    list_display = ('name', 'location','contact_number')
    ordering = ('name',)

