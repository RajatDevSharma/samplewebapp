# Generated by Django 4.0.4 on 2022-05-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_institute_skill_specialization_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='other_phone',
            field=models.TextField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='resume_path',
            field=models.TextField(null=True),
        ),
    ]