# Generated by Django 4.1.4 on 2023-01-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=75, unique=True)),
                ('password', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('ethnicity', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('hobbies', models.TextField()),
                ('occupation', models.CharField(max_length=32)),
                ('image', models.TextField()),
            ],
        ),
    ]
