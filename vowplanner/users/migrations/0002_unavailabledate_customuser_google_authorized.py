# Generated by Django 5.1.6 on 2025-03-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnavailableDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='google_authorized',
            field=models.BooleanField(default=False),
        ),
    ]
