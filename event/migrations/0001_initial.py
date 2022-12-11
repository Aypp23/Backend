# Generated by Django 3.2.8 on 2022-12-10 02:09

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.CharField(choices=[('Bio', 'Biotechnology'), ('Medicine', 'Medicinal plants and drug development'), ('Conservation', 'Conservation and utilization of our natural heritage'), ('Energy', 'Energy and Mineral Resources'), ('Environmental', 'Environmental Pollution and Remediation'), ('Science', 'Science and security'), ('IT', 'Information technology'), ('Agriculture', 'Agriculture and Food Security'), ('Nanotech', 'Nanotechnology'), ('Computational', 'Computational/Mathematical modeling'), ('Aquaculture', 'Aquaculture and the Blue Economy ')], max_length=100)),
                ('abstract', ckeditor_uploader.fields.RichTextUploadingField()),
                ('submitted', models.DateField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=140)),
            ],
        ),
    ]