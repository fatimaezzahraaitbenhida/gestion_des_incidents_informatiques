# Generated by Django 3.2.2 on 2023-08-22 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_alter_incident_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='dateDeclaration',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
