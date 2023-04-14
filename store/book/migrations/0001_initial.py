# Generated by Django 4.1.7 on 2023-04-01 20:14

import book.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, storage=book.models.AuthorPhotoStorage(), upload_to='author_photo/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, max_length=3200, verbose_name='Bio')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, storage=book.models.BookImageStorage(), upload_to='book_image/')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=1000)),
                ('genre', models.CharField(choices=[('Drama', 'Drama'), ('Mystery', 'Mystery'), ('Fantasy', 'Fantasy'), ('Historical', 'Historical'), ('Horror', 'Horror'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('Comedy', 'Comedy'), ('Science', 'Science'), ('Romance', 'Romance')], max_length=20)),
                ('available', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.author')),
            ],
        ),
    ]