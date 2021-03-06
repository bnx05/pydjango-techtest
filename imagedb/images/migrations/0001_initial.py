# Generated by Django 3.0.3 on 2020-02-10 01:22

from django.db import migrations, models
import django.db.models.deletion
import imagedb.images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=imagedb.images.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='ImageLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(db_index=True, max_length=255)),
                ('confidence', models.FloatField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='images.Image')),
            ],
        ),
    ]
