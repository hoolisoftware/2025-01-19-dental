# Generated by Django 5.1.5 on 2025-01-28 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_servicecategory_remove_serviceprice_service_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicecategory',
            options={'verbose_name': 'Hizmet kategorisi', 'verbose_name_plural': 'Hizmet kategorileri'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
    ]
