# Generated by Django 4.2.6 on 2023-11-03 04:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('data', models.DateField(auto_now_add=True)),
                ('invoice', models.CharField(blank=True, max_length=150, null=True)),
                ('contract_number', models.CharField(blank=True, max_length=150, null=True)),
                ('note', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ['-created_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IncomingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(blank=True, max_length=150, null=True)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outgoing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.CharField(editable=False, max_length=10, unique=True)),
                ('data', models.DateField()),
                ('type', models.CharField(choices=[('расход', 'расход'), ('продажа', 'продажа'), ('перемешения', 'перемешения')], default='перемешения')),
                ('note', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ['-created_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutgoingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(blank=True, max_length=150, null=True)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]