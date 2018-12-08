# Generated by Django 2.1.4 on 2018-12-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('introduction', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Ontology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('uri', models.URLField()),
                ('description', models.TextField(max_length=1000)),
                ('file', models.FileField(blank=True, upload_to='uploads/ontologies/')),
                ('license', models.CharField(blank=True, max_length=100)),
                ('authors', models.ManyToManyField(blank=True, to='waterdata.Author')),
            ],
        ),
    ]
