# Generated by Django 3.0.5 on 2020-04-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
