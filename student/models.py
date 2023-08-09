from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Transgender", "Transgender"),
    ]

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.first_name, filename)

class BloodGroup(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Hobbies'


class Student(models.Model):
    student_pk = models.BigAutoField(primary_key=True)
    first_name = models.CharField("Student's First Name", max_length=30, null=False, help_text="First name of the Student")
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    dob = models.DateField(verbose_name="Date of Birth", null=True, blank=True)
    age = models.IntegerField(help_text="Age will be calculated from DOB if given", null=True, blank=True)
    gender = models.CharField(max_length=11, choices=GENDER_CHOICES)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, blank=True, null=True)
    upload = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    is_disabled = models.BooleanField(blank=True, null=True, default=False, verbose_name="Are you physically disabled?")
    hobbies = models.ManyToManyField(Hobby, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name if self.last_name else self.first_name

    class Meta:
        # db_table_comment = "Student Details" # Only in django 4.2
        db_table = "student"
        ordering = ["student_pk"]
        # constraints = [
        #     models.CheckConstraint(check=models.Q(age__gte=18), name="age_gte_18"),
        # ]
        verbose_name = "Student"
        verbose_name_plural = "students"

    def clean(self):
        if self.age and self.age <= 18:
            raise ValidationError(_("Age must be greater than 18"))
        if self.gender == "Male":
            self.last_name = 'Male'
        elif self.gender == "Female":
            self.last_name = "Female"

