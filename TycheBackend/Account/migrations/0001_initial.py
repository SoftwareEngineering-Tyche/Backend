# Generated by Django 4.0.3 on 2022-04-14 14:31

import Account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logoimage', models.ImageField(upload_to='')),
                ('Featuredimage', models.ImageField(upload_to='')),
                ('Bannerimage', models.ImageField(upload_to='')),
                ('Name', models.CharField(max_length=200)),
                ('URL', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=900)),
                ('category', models.CharField(max_length=200)),
                ('DisplayTheme', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkArt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Account.models.upload_to, verbose_name='Image')),
                ('Externallink', models.URLField()),
                ('Description', models.CharField(max_length=200)),
                ('Supply', models.IntegerField()),
                ('BlockChain', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='account',
            fields=[
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.CharField(blank=True, max_length=500, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=Account.models.upload_to, verbose_name='Image')),
                ('banner', models.ImageField(blank=True, null=True, upload_to=Account.models.upload_to, verbose_name='Image')),
                ('socials', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('WalletInfo', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('collection', models.ManyToManyField(related_name='collections', to='Account.collection', verbose_name='members')),
                ('favorite', models.ManyToManyField(related_name='favorites', to='Account.workart', verbose_name='members')),
            ],
        ),
    ]
