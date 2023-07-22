# Generated by Django 4.2.3 on 2023-07-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
