# Generated by Django 5.0.6 on 2024-05-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivarity_description_alter_chaivarity_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='price',
            field=models.CharField(default='', max_length=2),
        ),
    ]
