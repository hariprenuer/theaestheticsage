# Generated by Django 4.2 on 2023-04-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=7)),
                ('date', models.IntegerField(max_length=2)),
                ('month', models.IntegerField(max_length=2)),
                ('year', models.IntegerField(max_length=4)),
                ('hour', models.IntegerField(max_length=2)),
                ('minutes', models.IntegerField(max_length=2)),
            ],
        ),
    ]
