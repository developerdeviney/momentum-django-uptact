# Generated by Django 3.1.1 on 2020-10-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
