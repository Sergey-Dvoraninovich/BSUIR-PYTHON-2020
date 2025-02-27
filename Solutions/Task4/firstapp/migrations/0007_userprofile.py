# Generated by Django 3.0.5 on 2020-04-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_building_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('profile_text', models.TextField()),
                ('profile_title', models.CharField(max_length=300)),
            ],
        ),
    ]
