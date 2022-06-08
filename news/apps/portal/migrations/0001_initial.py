# Generated by Django 4.0.5 on 2022-06-07 15:30

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
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='url')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('biography', models.TextField(blank=True)),
                ('birthday', models.DateField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('job', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='url')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='url')),
                ('title', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='url')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='url')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('views', models.PositiveIntegerField(default=0)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Update')),
                ('authors', models.ManyToManyField(to='portal.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.category')),
                ('tags', models.ManyToManyField(blank=True, to='portal.tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='author',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.organization'),
        ),
    ]
