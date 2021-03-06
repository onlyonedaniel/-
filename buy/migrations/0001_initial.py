# Generated by Django 2.1.1 on 2018-09-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('picture', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=30)),
                ('newprice', models.CharField(max_length=30)),
                ('mileage', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('picture', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=30)),
                ('newprice', models.CharField(max_length=30)),
                ('mileage', models.CharField(max_length=30)),
                ('orderno', models.CharField(db_column='orderNo', max_length=30)),
                ('orderstatus', models.IntegerField(db_column='orderStatus')),
                ('isdelete', models.IntegerField(db_column='isDelete')),
            ],
            options={
                'db_table': 'Orders',
                'managed': False,
            },
        ),
    ]
