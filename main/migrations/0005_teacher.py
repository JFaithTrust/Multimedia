# Generated by Django 4.0.4 on 2022-05-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact_rename_news_comment_news_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Imgs')),
                ('bio', models.CharField(max_length=200)),
                ('pthone_number', models.CharField(max_length=30)),
            ],
        ),
    ]