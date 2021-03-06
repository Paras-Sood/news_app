# Generated by Django 4.0 on 2021-12-30 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=500, null=True)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=5000, null=True)),
                ('content', models.CharField(max_length=20000)),
                ('publishedAt', models.DateTimeField()),
                ('url', models.URLField(unique=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='backend.source')),
            ],
        ),
    ]
