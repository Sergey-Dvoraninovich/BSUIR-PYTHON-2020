# Generated by Django 3.0.5 on 2020-04-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='products/')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photoes'),
        ),
    ]
