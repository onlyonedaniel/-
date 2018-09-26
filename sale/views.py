from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import random
# Create your views here.
def index(request):
  brand_list=Brand.objects.filter(isdelete=0).order_by('-id')
  popular_list=random.sample(list(Carinfo.objects.filter(ispurchase=0,isdelete=0)),5)
  return render(request,'index.html',locals())
#查看汽车详情的处理试图
def detail(request):
  carid=request.GET['carid']
  try:
    cardetail=Carinfo.objects.filter(id=carid)
  except ObjectDoesNotExist as e:
    return HttpResponse(e)
  #处理最近浏览
  if request.COOKIES.get('Recently_Viewed',''):
    #cookies中有最近浏览的信息
    cookie_car=request.COOKIES.get('Recently_Viewed')
    list_car=cookie_car.split(',')
    #如果list_car中已经有carid,则将其删除
    if carid in list_car:
      list_car.remove(carid)
    #判断浏览记录的数量是否大于等于２
    if len(list_car)>=2:
      list_car.pop()
    list_car=[carid]+list_car
    cookie_car_new=','.join(list_car)
  else:
    #cookies中没有最进浏览信息
    cookie_car_new=carid
  resp = render(request, 'detail.html', locals())
  resp.set_cookie('Recently_Viewed',cookie_car_new,60*60)

  return resp
#价格区间视图
def price(request):
  price=request.GET['price']
  low_price,max_price=price.split('-')
  brand=request.GET.get('brand','')
  try:
    #如果是８０w＋的话
    brand_list=Brand.objects.all()
    if max_price=='1000':
      car_list=Carinfo.objects.filter(price__gte=80).filter(ispurchase=0,isdelete=0)
    else:
      car_list=Carinfo.objects.filter(price__gte=int(low_price),price__lte=int(max_price)).filter(ispurchase=0,isdelete=0)  # 如果没有品牌的话
    #如果品牌的话
    if brand:
      # brandid=Brand.objects.filter()
      car_list=car_list.filter(serbran__btitle=brand)
  except ObjectDoesNotExist as e:
    return HttpResponse(e)
  return render(request,'list.html',locals())
