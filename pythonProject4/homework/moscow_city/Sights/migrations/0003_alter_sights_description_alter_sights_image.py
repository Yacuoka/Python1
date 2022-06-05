# Generated by Django 4.0.4 on 2022-05-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sights', '0002_rename_skills_sights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sights',
            name='description',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='sights',
            name='image',
            field=models.ImageField(upload_to='Sights/images/'),
        ),
    ]
