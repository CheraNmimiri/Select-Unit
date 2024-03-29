from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid


class Lesson(models.Model):
    FIELD = [
        ("مهندسی", "مهندسی"),
        ("انسانی", "انسانی"),
        ("پزشکی", "پزشکی"),

    ]
    DAYS = [
        ("شنبه", "شنبه"),
        ("یک‌شنبه", "یک‌شنبه"),
        ("دوشنبه", "دوشنبه"),
        ("سه‌شنبه", "سه‌شنبه"),
        ("چهارشنبه", "چهارشنبه"),
        ("پنج‌شنبه", "پنج‌شنبه"),
        ("جمعه", "جمعه"),
    ]
    name = models.CharField(max_length=250, null=False)
    USERNAME_FIELD = 'name'
    unit = models.IntegerField(null=False)
    professor = models.CharField(null=False, max_length=250)
    College = models.CharField(max_length=50, choices=FIELD)
    day = models.CharField(choices=DAYS, max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    
    ROLE = [
        ("admin", "Admin"),
        ("student", "Student"),
    ]
    
    GENDER = [
        ("M", "Man"),
        ("W", "Woman"),
        ("N", "none"),
    ]

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = 'id'
    full_name = models.CharField(max_length=250)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(choices=GENDER, max_length=100)
    birth_date = models.DateField()
    id_number = models.CharField(max_length=20, validators=[RegexValidator(r'^\d+$')])
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{11}$')])
    student_number = models.CharField(max_length=20, validators=[RegexValidator(r'^\d+$')])
    password = models.CharField(null=False, blank=False,max_length=100)
    lesson = models.ManyToManyField("Lesson")
    is_superuser = models.BooleanField(default=False, null=False, blank= False)    

    def __str__(self):
        return self.full_name

