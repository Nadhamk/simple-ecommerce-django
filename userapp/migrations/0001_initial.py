# Generated by Django 5.0 on 2023-12-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('address', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
