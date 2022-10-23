# Generated by Django 4.1.2 on 2022-10-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_classes', '0003_alter_course_catalog_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='catalog_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='class_capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='course',
            name='enrollment_available',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='enrollment_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='wait_cap',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='wait_list',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]