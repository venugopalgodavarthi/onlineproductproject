# Generated by Django 4.0.1 on 2022-01-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothdetail',
            name='cimg',
            field=models.ImageField(default='i.jpg', upload_to='cloths'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grocarydetail',
            name='gimg',
            field=models.ImageField(default='i.jpg', upload_to='grocary'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mobiledetail',
            name='mimg',
            field=models.ImageField(default='i.jpg', upload_to='product'),
            preserve_default=False,
        ),
    ]
