# Generated by Django 4.2.6 on 2023-11-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depo', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incoming',
            name='status',
        ),
        migrations.AddField(
            model_name='outgoing',
            name='status',
            field=models.CharField(blank=True, choices=[('Принят', 'Принят'), ('Отклонен', 'Отклонен'), ('В ожидании', 'В ожидании')], default='В ожидании', null=True),
        ),
    ]
