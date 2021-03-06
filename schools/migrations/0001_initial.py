# Generated by Django 4.0.5 on 2022-07-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npsn', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('people', models.IntegerField()),
                ('technology', models.IntegerField()),
                ('inovation', models.IntegerField()),
                ('self_development', models.IntegerField()),
            ],
        ),
    ]
