from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Applicant(AbstractUser):
    is_penn_student = models.BooleanField(default=False)
    application = models.OneToOneField('Application', on_delete=models.SET_NULL, null=True,
                                       blank=True, related_name='applicant_application')


class Application(models.Model):
    school_attending = models.CharField(max_length=50, default=None, null=True)
    student_year = models.CharField(max_length=20, default=None, null=True)
    student_major = models.CharField(max_length=50, default=None)
    phone_number = models.CharField(max_length=20, default=None, null=True)
    student_birthday = models.CharField(max_length=20, default=None, null=True)
    short_answer_1 = models.CharField(max_length=1000, default=None, null=True)
    short_answer_2 = models.CharField(max_length=1000, default=None, null=True)
    first_hackathon = models.CharField(max_length=20, default=None, null=True)
    team_member1 = models.CharField(max_length=100, default=None, null=True)
    team_member2 = models.CharField(max_length=100, default=None, null=True)
    team_member3 = models.CharField(max_length=100, default=None, null=True)
    STATUS_CHOICES = [
        ("ACPT", "Accepted"),
        ("RJCT", "Rejected"),
        ("WLST", "Waitlisted"),
        ("PROC", "Processing"),
    ]

    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="STRT")
