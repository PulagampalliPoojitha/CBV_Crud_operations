# Generated by Django 4.2.1 on 2023-08-07 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Scname', models.CharField(max_length=100)),
                ('Scprincipal', models.CharField(max_length=100)),
                ('Sclocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('Sage', models.IntegerField()),
                ('Scname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panda', to='app.school')),
            ],
        ),
    ]
