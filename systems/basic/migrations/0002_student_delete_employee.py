# Generated by Django 5.0.1 on 2024-01-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
