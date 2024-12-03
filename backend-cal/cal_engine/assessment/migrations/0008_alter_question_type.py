# Generated by Django 4.2.16 on 2024-12-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0007_delete_questionsolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('MCQ', 'Multiple Choice Question'), ('MSQ', 'Multiple Select Question'), ('NAT', 'Numerical Answer Type'), ('DESC', 'Descriptive Question')], max_length=20),
        ),
    ]
