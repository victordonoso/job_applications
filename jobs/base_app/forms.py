from locale import currency
from django.forms import ModelForm, Widget
from django.forms import Textarea, TextInput, Select, NumberInput, EmailInput, PasswordInput, CheckboxInput, RadioSelect, DateInput, TimeInput, DateTimeInput, URLInput
from djmoney.forms.widgets import MoneyWidget
from django.utils.translation import gettext as _


from .models import JobApplications, ReminderModel

class JobApplicationForm(ModelForm):
    class Meta:
        model = JobApplications
        fields = ['job_company', 'job_title', 'job_description', 'contract_type', 'job_location', 'job_industry', 'other_industry', 'job_profession', 'other_profession', 'job_salary']

        widgets = {
            'job_company': TextInput(attrs={'class': 'form-control'}),
            'job_title': TextInput(attrs={'class': 'form-control'}),
            'job_description': Textarea(attrs={'class': 'form-control'}),
            'contract_type': Select(attrs={'class': 'form-control'}),
            'job_location': TextInput(attrs={'class': 'form-control'}),
            'job_industry': Select(attrs={'class': 'form-control'}),
            'other_industry': TextInput(attrs={'class': 'form-control'}),
            'job_profession': Select(attrs={'class': 'form-control'}),
            'other_profession': TextInput(attrs={'class': 'form-control'}),
            'job_salary': MoneyWidget(attrs={'class': 'form-control'}),
        }
        """help_texts = {
            'job_company': _('Job offering company'),
            'job_title': _('Job title'),
            'job_description': _('Job description'),
            'contract_type': _('Contract type'),
            'job_location': _('Job location'),
            'job_industry': _('Select the job industry'),
            'other_industry': _('If not on the list, enter the industry name'),
            'job_profession': _('Select the job knowledge area'),
            'other_profession': _('If not on the list, enter the knowledge area name'),
            'job_salary': _('Enter the expected or agreed salary'),
        }"""
        labels = {
            'job_company': _('Job offering company'),
            'other_industry': _('Other...'),
            'other_profession': _('Other...'),
        }



class ReminderForm(ModelForm):
    class Meta:
        model = ReminderModel
        fields = ['reminder_type', 'reminder_status', 'reminder_description', 'reminder_date', 'reminder_time', 'reminder_contact_name', 'reminder_contact_email', 'reminder_contact_number', 'reminder_notes', 'reminder_url']
        labels = {
            'reminder_type': _('Type'),
            'reminder_status': _('Status'),
            'reminder_description': _('Description'),
            'reminder_date': _('Date'),
            'reminder_time': _('Time'),
            'reminder_contact_name': _('Contact name'),
            'reminder_contact_email': _('Contact email'),
            'reminder_contact_number': _('Contact number'),
            'reminder_notes': _('Notes'),
            'reminder_url': _('Appointment URL'),
        }
        widgets = {
            'reminder_type': Select(attrs={'class': 'form-control'}),
            'reminder_status': Select(attrs={'class': 'form-control'}),
            'reminder_description': Textarea(attrs={'class': 'form-control'}),
            'reminder_date': DateInput(attrs={'class': 'form-control'}),
            'reminder_time': TimeInput(attrs={'class': 'form-control'}),
            'reminder_contact_name': TextInput(attrs={'class': 'form-control'}),
            'reminder_contact_email': EmailInput(attrs={'class': 'form-control'}),
            'reminder_contact_number': TextInput(attrs={'class': 'form-control'}),
            'reminder_notes': Textarea(attrs={'class': 'form-control'}),
            'reminder_url': URLInput(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'reminder_type': _('Select the reminder type'),
            'reminder_status': _('Select status'),
            'reminder_description': _('Enter a description (required)'),
            'reminder_contact_name': _('i.e.: Alex Smith'),
            'reminder_contact_email': _('i.e.: alexsmith@example.com'),
            'reminder_contact_number': _('i.e.: +44 7123456789'),
            'reminder_notes': _('Enter any additional notes'),
            'reminder_url': _('Enter a link (if applicable)'),
        }
        error_messages = {
            'reminder_type': {
                'required': _("This field is required"),
            },
            'reminder_status': {
                'required': _("This field is required"),
            },
            'reminder_description': {
                'required': _("This field is required"),
            },
            'reminder_contact_name': {
                'max_length': _("This field has max length of 100 characters"),
            },
            'reminder_contact_number': {
                'max_length': _("This field has max length of 100 characters"),
            },
        }
