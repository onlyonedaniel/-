import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
#车辆品牌列表相关
from buy.models import Cart, Orders
from sale.models import Brand, Carinfo
from userinfo.models import Users


def brandlist(request):
    #接受传递过来的brand信息
    brand=request.GET['brand']
    try:

        #查询所有的品牌列表
        brand_list=Brand.objects.all()
        #通过品牌的信息过获取品牌对象
        brand1=Brand.objects.get(btitle=brand)
        #查询Brand下所有的车辆信息
        car_list=brand1.carinfo_set.filter(ispurchase=0,isdelete=0)
        print(car_list)
        params={'brand':brand,'brand_list': brand_list, 'car_list': car_list}
    except ObjectDoesNotExist as e:
        return HttpResponse(e)
    return render(request,'list.html',params)
def add_order(request):
    if request.user.is_authenticated:
        car_id=request.GET['carid']
        car=Carinfo.objects.get(id=int(car_id))
        cart=Cart()
        cart.brand=car.serbran.btitle+car.ctitle
        cart.picture=car.picture
        cart.price=car.price
        cart.newprice=car.newprice
        cart.mileage=car.mileage
        cart.car=car
        cart.suser=request.user
        try:
            cart.save()
        except ObjectDoesNotExist as e:
            return HttpResponse(e)
        return render(request,'order.html',locals())
    else:
        return render(request,'login.html')
def del_order(request):
    user_id=request.user.id
    car_id=request.GET['carid']
    try:
        cart=Cart.objects.get(car_id=int(car_id),suser_id=int(user_id))
        cart.delete()
    except ObjectDoesNotExist as e:
        return HttpResponse(e)
    return redirect('/')
def confirm_buy(request):
    if request.user.is_authenticated:
        car_id=request.GET['carid']
        orderNO=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        cart=Cart.objects.filter(car_id=car_id)[0]
        car=Carinfo.objects.filter(id=car_id)[0]
        brand=cart.brand
        picture=cart.picture
        newprice=cart.newprice
        mileage=cart.mileage
        price=cart.price
        sale_user=car.user
        buy_user=request.user
        Orders.objects.create(sale_user=sale_user,buy_user=buy_user,
                              brand=brand,picture=picture,price=price,
                              newprice=newprice,mileage=mileage,
                              orderno=orderNO)
        #查询当前登录账户的所有订单
        #查询当前登录用户信息
        #查询当前登录用户所卖的车
        user_id=request.user.id
        orders=Orders.objects.filter(buy_user=user_id).order_by('-id')
        for order in orders:
            print(order.orderno)
        user=Users.objects.get(id=user_id)
        #查询当前登录用户所卖的车
        car=Carinfo.objects.filter(user_id=user_id,ispurchase=0,isdelete=0)
        # 查询当前用户的最近浏览记录
        rec_view_list = []
        if request.COOKIES.get('Recently_Viewed', ''):
            cookie_car = request.COOKIES.get('Recently_Viewed', '')
            car_id = cookie_car.split(',')
            for id in car_id:
                rec_view_list.append(Carinfo.objects.get(id=id))
            print(rec_view_list)
        return render(request,'user-info.html',{'orders':locals()})
    else:
        return redirect('login')
