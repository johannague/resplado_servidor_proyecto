# Generated by Django 4.0.2 on 2022-02-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
            },
        ),
        migrations.AlterModelOptions(
            name='pelicula',
            options={'verbose_name': 'Película', 'verbose_name_plural': 'Películas'},
        ),
        migrations.AddField(
            model_name='pelicula',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='generos',
            field=models.ManyToManyField(to='pelis.Genre'),
        ),
    ]