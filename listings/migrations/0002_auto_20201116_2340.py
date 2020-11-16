# Generated by Django 3.1.3 on 2020-11-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='college',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='rating',
            new_name='bathrooms',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='months',
            new_name='bedrooms',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='weeks',
            new_name='garage',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='years',
            new_name='sqft',
        ),
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
