# Generated by Django 4.0.4 on 2022-07-13 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=4, max_digits=14)),
            ],
        ),
    ]