# Generated by Django 4.2 on 2023-12-10 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_place_rating_constraint_place_latitude_constraint_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direction', models.FloatField()),
                ('air_pressure', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.place')),
            ],
        ),
    ]