# Generated by Django 3.1.2 on 2021-05-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0003_auto_20210508_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='review_std',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('clg_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
