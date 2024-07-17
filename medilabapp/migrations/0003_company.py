# Generated by Django 5.0.6 on 2024-07-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medilabapp', '0002_patient_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('phone', models.CharField(max_length=200)),
                ('staff', models.IntegerField()),
            ],
        ),
    ]