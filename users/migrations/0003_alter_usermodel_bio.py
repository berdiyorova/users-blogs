# Generated by Django 5.1.2 on 2024-10-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='bio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
