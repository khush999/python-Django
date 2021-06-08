# Generated by Django 3.1.2 on 2021-03-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('SID', models.AutoField(primary_key=True, serialize=False)),
                ('F_name', models.CharField(max_length=50)),
                ('L_name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('Pin_code', models.IntegerField()),
                ('Birth_Date', models.DateField()),
                ('Gender', models.CharField(max_length=20)),
                ('Mobile_no', models.IntegerField()),
                ('Email', models.EmailField(max_length=100)),
                ('Enroll_No', models.IntegerField()),
                ('college_Name', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]