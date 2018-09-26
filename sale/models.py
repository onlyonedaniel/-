from django.db import models
from userinfo import models as md
# Create your models here.
class Brand(models.Model):
  logo_brand = models.CharField(max_length=100)
  btitle = models.CharField(max_length=30)
  isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

  class Meta:
    managed = False
    db_table = 'Brand'


# 购物车
class Carinfo(models.Model):
  #车名，上牌日期，发动机号，公里数，维修记录，期望售价，成交价格，新车价格，图片，照片，手续，债务，买家承诺
  #审核进度，是否购买成交，车辆型号，用户，是否删除
  ctitle = models.CharField(max_length=30)
  regist_date = models.DateField()
  engineno = models.CharField(db_column='engineNo', max_length=30)  # Field name made lowercase.
  mileage = models.IntegerField()
  maintenance_record = models.CharField(max_length=10)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  extractprice = models.DecimalField(max_digits=8, decimal_places=2,default=0)
  newprice = models.DecimalField(max_digits=8, decimal_places=2)
  #需要将charfield改为imagefield
  picture = models.ImageField(max_length=100,upload_to='img/car')
  formalities = models.CharField(max_length=10)
  debt = models.CharField(max_length=10)
  promise = models.TextField(blank=True, null=True)
  examine = models.CharField(max_length=30)
  #是否成交，增加默认值 default=0
  ispurchase = models.IntegerField(db_column='isPurchase',default=0)  # Field name made lowercase.
  serbran = models.ForeignKey(Brand, models.DO_NOTHING)
  user = models.ForeignKey(md.Users, models.DO_NOTHING)
  #是否删除，择交默认值default=0
  isdelete = models.IntegerField(db_column='isDelete',default=0)  # Field name made lowercase.

  class Meta:
    managed = False
    db_table = 'Carinfo'
