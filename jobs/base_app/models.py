from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.translation import gettext as _


class IndustryList(models.Model):

    industry_name = models.CharField(max_length=100, verbose_name=_("Industry Name"))
    industry_description = models.TextField(verbose_name=_("Industry Description"))

    class Meta:
        verbose_name = _("Industry List")
        verbose_name_plural = _("Industry Lists")

    def __str__(self):
        return self.industry_name

    def get_absolute_url(self):
        return reverse("IndustryList_detail", kwargs={"pk": self.pk})

class KnowledgeAreas(models.Model):

    area_name = models.CharField(max_length=200, verbose_name=_("Area Name"))
    area_description = models.TextField(verbose_name=_("Area Description"))

    class Meta:
        verbose_name = _("Knowledge Area")
        verbose_name_plural = _("Knowledge Areas")

    def __str__(self):
        return self.area_name

    def get_absolute_url(self):
        return reverse("KnowledgeAreas_detail", kwargs={"pk": self.pk})



class JobTypes(models.Model):

    type_name = models.CharField(max_length=100, verbose_name=_("Type Name"))
    type_description = models.TextField(verbose_name=_("Type Description"))

    class Meta:
        verbose_name = _("JobTypes")
        verbose_name_plural = _("JobTypess")

    def __str__(self):
        return self.type_name

    def get_absolute_url(self):
        return reverse("JobTypes_detail", kwargs={"pk": self.pk})



class JobApplications(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    job_company = models.CharField(max_length=150, verbose_name=_("Job Company"))
    job_title = models.CharField(max_length=200, verbose_name=_("Job Title"))
    job_description = models.TextField(verbose_name=_("Job Description"))
    job_location = models.CharField(max_length=300, verbose_name=_("Job Location"))
    job_type = models.ForeignKey(JobTypes, on_delete=models.CASCADE, verbose_name=_("Job Type"))
    job_industry = models.ForeignKey(IndustryList, on_delete=models.CASCADE, verbose_name=_("Industry"))
    job_knowledge_area = models.ForeignKey(KnowledgeAreas, on_delete=models.CASCADE, verbose_name=_("Knowledge Area"))
    job_salary = models.DecimalField(_("Salary"), max_digits=9, decimal_places=2)
    SALARY_CHOICES = [
        ('MO', _('Monthly')),
        ('YR', _('Yearly')),
        ('DY', _('Daily')),
        ('HR', _('Hourly')),
        ('NO', _('Not Specified')),
        ('OT', _('Other')),
    ]
    salary_type = models.CharField(max_length=2, choices=SALARY_CHOICES, default='MO', verbose_name=_("Salary Type"), null=True, blank=True)
    CONTRACT_CHOICES = [
        ('FT', _('Full Time')),
        ('PT', _('Part Time')),
        ('CO', _('Contract')),
        ('IN', _('Internship')),
        ('NO', _('Not Specified')),
        ('OT', _('Other')),
    ]
    contract_type = models.CharField(max_length=2, choices=CONTRACT_CHOICES, default='FT', verbose_name=_("Contract Type"), null=True, blank=True)
    job_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    
    class Meta:
        verbose_name = _("Job Application")
        verbose_name_plural = _("Job Applications")

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse("JobApplications_detail", kwargs={"pk": self.pk})


class ReminderModel(models.Model):

    parent_job = models.ForeignKey(JobApplications, on_delete=models.CASCADE, verbose_name=_("Job"))
    REMINDER_CHOICES = [
        ('INT', _('Interview')),
        ('CALL', _('Call')),
        ('EMAIL', 'Email'),
        ('OTHER', 'Other'),
    ]
    reminder_type = models.CharField(max_length=4, choices=REMINDER_CHOICES, default='INT', verbose_name=_("Type"))
    REMINDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    reminder_status = models.CharField(max_length=10, choices=REMINDER_STATUS_CHOICES, default='PENDING', verbose_name=_("Status"))
    reminder_date = models.DateField(verbose_name=_("Date"))
    reminder_time = models.TimeField(verbose_name=_("Time"))
    reminder_contact_name = models.CharField(max_length=100, verbose_name=_("Contact Name"), null=True, blank=True)
    reminder_contact_number = models.CharField(max_length=100, verbose_name=_("Contact Number"), null=True, blank=True)
    reminder_contact_email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)
    reminder_description = models.TextField(verbose_name=_("Description"))
    reminder_notes = models.TextField(verbose_name=_("Notes"), null=True, blank=True)    

    class Meta:
        verbose_name = _("Reminder Model")
        verbose_name_plural = _("Reminder Models")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ReminderModel_detail", kwargs={"pk": self.pk})
