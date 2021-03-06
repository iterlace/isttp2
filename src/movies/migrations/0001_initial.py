# Generated by Django 4.0.4 on 2022-05-29 20:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64)),
            ],
            options={
                'verbose_name': 'Petition',
                'verbose_name_plural': 'Petitions',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=256)),
                ('director', models.TextField(max_length=256)),
                ('release_year', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movies.category', verbose_name='Petition')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'db_table': 'movies',
            },
        ),
    ]
