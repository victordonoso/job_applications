import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django_htmx.http import trigger_client_event

from .forms import JobApplicationForm, ReminderForm

from .models import JobApplications, ReminderModel

class MyJobs(LoginRequiredMixin, TemplateView):
    template_name = 'base_app/my_jobs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = JobApplications.objects.filter(app_user=self.request.user)
        for job in context['jobs']:
            job.reminders = ReminderModel.objects.filter(parent_job=job)
        return context

def jobs_table(request):
    jobs = JobApplications.objects.filter(app_user=request.user)
    for job in jobs:
        job.reminders = ReminderModel.objects.filter(parent_job=job)
    return render(request, 'base_app/my_jobs.html', {'jobs': jobs})

def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.app_user = request.user
            job.save()
            job_list = JobApplications.objects.filter(app_user=request.user)
            for job in job_list:
                job.reminders = ReminderModel.objects.filter(parent_job=job)
            response = render(request, 'base_app/my_jobs.html', {'jobs': job_list})
            trigger_client_event(response, 'updateMyJobs', {})
            return response
    form = JobApplicationForm()
    return render(request, 'base_app/add_job.html', {'form': form})

def edit_job(request, pk):
    object = JobApplications.objects.get(pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=object)
        if form.is_valid():
            job = form.save(commit=False)
            job.app_user = request.user
            job.save()
            return jobs_table(request)
    form = JobApplicationForm(instance=object)
    return render(request, 'base_app/edit_job.html', {'form': form, 'object': object})

def delete_job(request, pk):
    job = JobApplications.objects.get(pk=pk)
    job.delete()
    return jobs_table(request)