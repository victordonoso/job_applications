from django.urls import path
from .views import MyJobs, add_job, edit_job

urlpatterns = [
    path('my_jobs/', MyJobs.as_view(), name='my_jobs'),
    path('add_job/', add_job, name='add_job'),
    path('edit_job/<int:pk>', edit_job, name='edit_job'),
]
