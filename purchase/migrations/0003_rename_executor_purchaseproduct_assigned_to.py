# Generated by Django 4.2.6 on 2023-12-02 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseproduct',
            old_name='executor',
            new_name='assigned_to',
        ),
    ]