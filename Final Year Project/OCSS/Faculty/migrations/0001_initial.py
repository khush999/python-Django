# Generated by Django 3.1.2 on 2021-03-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('FID', models.AutoField(primary_key=True, serialize=False)),
                ('F_name', models.CharField(max_length=50)),
                ('L_name', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
    ]
