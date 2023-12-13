# Generated by Django 4.2.6 on 2023-12-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('arrival_date', models.DateField()),
                ('status', models.CharField(choices=[('new', 'Новая'), ('confirmed', 'Подтверждена'), ('assigned', 'Распределена'), ('rejected', 'Отклонена'), ('accepted', 'Принята'), ('delivered', 'Доставлена'), ('in_stock', 'В складе')], default='new', max_length=20)),
                ('note', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'ordering': ['-created_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('signed_at', models.DateTimeField(blank=True, null=True)),
                ('rejected_at', models.DateTimeField(blank=True, null=True)),
                ('assigned_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('new', 'Новая'), ('confirmed', 'Подтверждена'), ('assigned', 'Распределена'), ('rejected', 'Отклонена'), ('accepted', 'Принята'), ('delivered', 'Доставлена'), ('in_stock', 'В складе')], default='new', max_length=50)),
            ],
        ),
    ]
