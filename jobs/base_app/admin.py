from django.contrib import admin
from .models import IndustryList, JobApplications, Professions, ReminderModel

# Register your models here.
@admin.register(JobApplications, ReminderModel, IndustryList, Professions)

class JobApplicationsAdmin(admin.ModelAdmin):
    pass

