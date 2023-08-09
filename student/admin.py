from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(BloodGroup)
class BloodGroupAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ['student_pk', 'first_name', 'last_name', 'gender', 'blood_group', 'dob', 'upload']
    list_filter = ['blood_group', 'gender']
    empty_value_display = "-- NA --"
