# Generated by Django 4.0.8 on 2022-10-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AptDetails',
            fields=[
                ('adv_id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('city_id', models.CharField(max_length=50)),
                ('district_id', models.CharField(max_length=50)),
                ('region_id', models.CharField(max_length=50)),
                ('time_created', models.CharField(max_length=50)),
                ('time_valid_to', models.CharField(max_length=50)),
                ('is_business', models.TextField()),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=50)),
                ('furniture', models.CharField(max_length=50)),
                ('market', models.CharField(max_length=50)),
                ('builttype', models.CharField(max_length=50)),
                ('meters', models.CharField(max_length=50)),
                ('rooms', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AptPrices',
            fields=[
                ('update_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('adv_id', models.CharField(blank=True, max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('highlighted', models.TextField()),
                ('urgent', models.TextField()),
                ('top_ad', models.TextField()),
                ('date', models.TextField()),
                ('city_id', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('city_id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('city_name', models.TextField()),
                ('region_id', models.CharField(max_length=50)),
                ('population', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('district_id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('district_name', models.TextField(blank=True, null=True)),
                ('city_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('region_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('region_name', models.TextField()),
            ],
        ),
    ]
