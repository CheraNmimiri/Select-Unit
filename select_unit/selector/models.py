from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid


class Student(models.Model):
    GENDER = [
        ("M", "Man"),
        ("W", "Woman"),
        ("N", "none"),
    ]

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    full_name = models.CharField(max_length=250)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(choices=GENDER, max_length=100)
    birth_date = models.DateField()
    student_number = models.CharField(max_length=20, validators=[RegexValidator(r'^\d$')])
    card_number = models.CharField(max_length=20, validators=[RegexValidator(r'^\d$')])
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{11}$')])

    def __str__(self):
        return self.full_name


class Meta:
    ordering = ['last_name']
