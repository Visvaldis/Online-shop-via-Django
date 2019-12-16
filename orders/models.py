from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    summa = models.FloatField()
    customer = models.ForeignKey(User, models.CASCADE)
    session_key = models.CharField(max_length=256)
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tOrder'


class OrderDetails(models.Model):
    details_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    product_amount = models.FloatField()
    summa = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tOrder_details'
