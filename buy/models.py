from django.db import models
from sale import models as sm
from userinfo import models as um
# Create your models here.
class Cart(models.Model):
  brand = models.CharField(max_length=30)
  picture = models.CharField(max_length=100)
  price = models.CharField(max_length=30)
  newprice = models.CharField(max_length=30)
  mileage = models.CharField(max_length=30)
  car = models.ForeignKey(sm.Carinfo, models.DO_NOTHING)
  suser = models.ForeignKey(um.Users, models.DO_NOTHING)

  class Meta:
    managed = False
    db_table = 'Cart'
ORDERSTATUS=(
  (1,'未付款'),(2,'已付款'),(3,'订单关闭'),
)

# 订单
class Orders(models.Model):
  brand = models.CharField(max_length=30)
  picture = models.CharField(max_length=100)
  price = models.CharField(max_length=30)
  newprice = models.CharField(max_length=30)
  mileage = models.CharField(max_length=30)
  orderno = models.CharField(db_column='orderNo', max_length=30)  # Field name made lowercase.
  orderstatus = models.IntegerField(db_column='orderStatus',choices=ORDERSTATUS,default=1)  # Field name made lowercase.
  buy_user = models.ForeignKey(um.Users, models.DO_NOTHING,related_name='buy_user_id')
  sale_user = models.ForeignKey(um.Users, models.DO_NOTHING,related_name='sale_user_id')
  isdelete = models.IntegerField(db_column='isDelete',default=0)  # Field name made lowercase.

  class Meta:
    managed = False
    db_table = 'Orders'