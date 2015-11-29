# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(serialize=False, primary_key=True)),
                ('identity_id', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('birthday', models.DateField()),
                ('education', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=11)),
                ('marriage', models.CharField(max_length=10)),
                ('province', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=60)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_id', models.IntegerField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.IntegerField(serialize=False, primary_key=True)),
                ('stock_date', models.DateField()),
                ('unit', models.CharField(max_length=20)),
                ('stock_price', models.FloatField()),
                ('stock_quantity', models.IntegerField()),
                ('buyer', models.ForeignKey(to='supermarket.Employee')),
                ('goods', models.ForeignKey(to='supermarket.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_salary', models.IntegerField()),
                ('bonus', models.IntegerField()),
                ('employee', models.ForeignKey(to='supermarket.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sales_id', models.IntegerField(serialize=False, primary_key=True)),
                ('unit', models.CharField(max_length=20)),
                ('sale_price', models.FloatField()),
                ('sale_quantity', models.IntegerField()),
                ('sale_date', models.DateField()),
                ('goods', models.ForeignKey(to='supermarket.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Supplyer',
            fields=[
                ('supplyer_id', models.IntegerField(serialize=False, primary_key=True)),
                ('supplyer_name', models.CharField(max_length=60)),
                ('supplyer_person', models.CharField(max_length=60)),
                ('supplyer_phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplyer',
            field=models.ForeignKey(to='supermarket.Supplyer'),
        ),
        migrations.AddField(
            model_name='goods',
            name='supplyer',
            field=models.ManyToManyField(to='supermarket.Supplyer'),
        ),
    ]
