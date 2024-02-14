from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin
from .models import Student, Lessone

class BarAdmin(admin.ModelAdmin):
    list_filter = (
        ('datetime', JDateFieldListFilter),
    )
class BarTimeAdmin(admin.ModelAdmin):
    list_filter = (
        ('datetime', JDateFieldListFilter),
    )


admin.site.register(Student)
admin.site.register(Lessone)