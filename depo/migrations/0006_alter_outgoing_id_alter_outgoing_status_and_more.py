# Generated by Django 4.2.6 on 2023-11-17 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depo', '0005_stock_material_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoing',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='outgoing',
            name='status',
            field=models.CharField(blank=True, choices=[('Принят', 'Принят'), ('Отклонен', 'Отклонен'), ('В ожидании', 'В ожидании')], default='В ожидании', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='outgoing',
            name='type',
            field=models.CharField(choices=[('расход', 'Расход'), ('продажа', 'Продажа'), ('перемешения', 'Перемещение')], default='перемешения', max_length=20),
        ),
        migrations.AlterField(
            model_name='outgoingmaterial',
            name='outgoing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_materials', to='depo.outgoing'),
        ),
    ]
