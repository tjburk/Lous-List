# Generated by Django 4.1.2 on 2022-10-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('instructor_name', models.CharField(max_length=50)),
                ('instructor_email', models.CharField(max_length=50)),
                ('course_number', models.IntegerField(primary_key=True, serialize=False)),
                ('semester_code', models.IntegerField()),
                ('subject', models.CharField(max_length=4)),
                ('catalog_number', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('units', models.CharField(max_length=5)),
                ('component', models.CharField(max_length=5)),
                ('class_capacity', models.IntegerField()),
                ('wait_list', models.IntegerField()),
                ('wait_cap', models.IntegerField()),
                ('enrollment_total', models.IntegerField()),
                ('enrollment_available', models.IntegerField()),
                ('topic', models.CharField(max_length=50)),
                ('meetings_days', models.CharField(max_length=10)),
                ('meetings_start_time', models.CharField(max_length=30)),
                ('meetings_end_time', models.CharField(max_length=30)),
                ('meetings_facility_description', models.CharField(max_length=100)),
            ],
        ),
    ]
