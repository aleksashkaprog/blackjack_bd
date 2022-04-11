# Generated by Django 4.0.2 on 2022-04-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=1000)),
                ('inv', models.IntegerField()),
                ('price', models.FloatField()),
                ('note', models.TextField()),
                ('qr', models.ImageField(upload_to='')),
            ],
        ),
    ]