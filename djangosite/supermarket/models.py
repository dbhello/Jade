from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(primary_key=True)
    identity_id = models.CharField(max_length=18)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    #password = models.CharField(max_length=100)
    education = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    marriage = models.CharField(max_length=10)
    province = models.CharField(max_length=30)
    address = models.CharField(max_length=60)


class Salary(models.Model): # need detail
    employee = models.ForeignKey(Employee)
    base_salary = models.IntegerField()
    bonus = models.IntegerField()


class Supplyer(models.Model):
    supplyer_id = models.IntegerField(primary_key=True)
    supplyer_name = models.CharField(max_length=60)
    supplyer_person = models.CharField(max_length=60)
    supplyer_phone = models.CharField(max_length=11)
    address = models.CharField(max_length=60)


class Goods(models.Model):
    goods_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    supplyer = models.ManyToManyField(Supplyer) # ###attention!


class Sales(models.Model):
    sales_id = models.IntegerField(primary_key=True)
    goods = models.ForeignKey(Goods)
    unit = models.CharField(max_length=20)
    sale_price = models.FloatField()
    sale_quantity = models.IntegerField()
    sale_date = models.DateField()


class Purchase(models.Model):
    purchase_id = models.IntegerField(primary_key=True)
    goods = models.ForeignKey(Goods)
    supplyer = models.ForeignKey(Supplyer)
    buyer = models.ForeignKey(Employee)
    stock_date = models.DateField()
    unit = models.CharField(max_length=20)
    stock_price = models.FloatField()
    stock_quantity = models.IntegerField()
