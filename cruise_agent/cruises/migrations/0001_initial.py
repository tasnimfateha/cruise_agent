# Generated by Django 4.1.7 on 2023-03-20 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('tonnage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('ship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cruises', to='cruises.ship')),
            ],
        ),
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('beds', models.IntegerField()),
                ('deck', models.IntegerField()),
                ('ship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabins', to='cruises.ship')),
            ],
        ),
    ]
