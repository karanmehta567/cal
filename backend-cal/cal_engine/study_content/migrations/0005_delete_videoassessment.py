# Generated by Django 4.2.16 on 2024-12-03 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_content', '0004_remove_videosegmentassessment_assessment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoAssessment',
        ),
    ]
