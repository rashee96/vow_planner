# Generated by Django 5.1.6 on 2025-03-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_vendorevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorevent',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
