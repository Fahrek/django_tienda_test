# Generated by Django 3.1.4 on 2020-12-16 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('new', models.BooleanField()),
                ('fabr_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suit.brand')),
            ],
        ),
    ]
