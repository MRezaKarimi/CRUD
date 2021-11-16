# Generated by Django 3.2 on 2021-11-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('birthday', models.CharField(max_length=50)),
                ('telephone_number', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]