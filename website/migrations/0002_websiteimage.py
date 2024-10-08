# Generated by Django 4.2.15 on 2024-08-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('hero', 'Hero Image'), ('background', 'Background Image'), ('menu', 'Menu Item Image'), ('gallery', 'Gallery Image')], max_length=20)),
                ('image_url', models.URLField(max_length=500)),
            ],
        ),
    ]
