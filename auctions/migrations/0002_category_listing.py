# Generated by Django 5.0.1 on 2024-01-15 10:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comments', models.CharField(max_length=500)),
                ('active', models.BooleanField()),
                ('wachlist', models.ManyToManyField(blank=True, null=True, related_name='wachlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
