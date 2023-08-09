# Generated by Django 3.2.20 on 2023-08-09 04:17

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_pk', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First name of the Student', max_length=30, verbose_name="Student's First Name")),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('age', models.IntegerField(blank=True, help_text='Age will be calculated from DOB if given', null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=11)),
                ('upload', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('is_disabled', models.BooleanField(blank=True, default=False, null=True, verbose_name='Are you physically disabled?')),
                ('blood_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.bloodgroup')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'students',
                'db_table': 'student',
                'ordering': ['student_pk'],
            },
        ),
    ]
