# Generated by Django 3.1.3 on 2020-11-16 14:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('years', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('months', models.IntegerField()),
                ('weeks', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='creators.creator')),
            ],
        ),
    ]