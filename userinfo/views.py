from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect

from buy.models import Orders
from userinfo.models import *
from sale.models import *
auth_check='MarcelArhut'
# Create your views here.
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        username=request.POST.get('username','')
        password=request.POST.get('userpwd','')
        if username and password:
            #利用django自带的方法验证登录信息
            user=auth.authenticate(username=username,password=password)
            if user and user.is_active:
                #把用户的信息保存进session
                auth.login(request,user)
                return HttpResponseRedirect('/')
            else:
                return render(request,'login.html',{'message':'用户名或密码不正确'})
        else:
            return render(request,'login.html',{'message':'用户名或密码不正确'})

def logout(request):
    auth.logout(request)
    return redirect('/')
#声明一个全局的new_user对象，用于表示要注册的用户信息
new_user=Users()
def register(request):
    if request.method=='GET':
        #查看注册页面
        return render(request,'register.html')
    else:
        #接收用户名和密码
        new_user.username=request.POST['username']
        #判断用户名称是否存在
        oldUser=Users.objects.filter(username=new_user.username)
        if len(oldUser)>0:
            return render(request,'register.html',{'message':'用户名已经存在'})
        #处理密码
        new_user.password=make_password(request.POST['userpwd'],auth_check,'pbkdf2_sha1')

        #处理注册信息
        if 'tobuy' in request.POST:
            return render(request,'buyregister.html')
        if 'tosale' in request.POST:
            return render(request,'info-message.html')

def buyinfo(request):
    #继续想new_user中追加注册信息，再将new_user保存回数据库
    if request.method=='POST':
        new_user.realname=request.POST['realname']
        new_user.uidentity=request.POST['identity']
        new_user.address=request.POST['address']
        new_user.cellphone=request.POST['phone']
        new_user.sex=request.POST['gender']
    try:
        new_user.save()
    except ObjectDoesNotExist as e:
        return HttpResponse(e)
    return redirect('/')

def infomes_in(request):
    if request.method=='POST':
        #获取用户信息插入到表中
        try:
            new_user.realname = request.POST['realname']
            new_user.uidentity = request.POST['identity']
            new_user.address = request.POST['address']
            new_user.cellphone = request.POST['phone']
            new_user.sex = request.POST['gender']
            new_user.save()
            #获取车辆信息插入carinfo中
            new_car=Carinfo()
            #获取brand的对象
            brand=Brand.objects.filter(btitle=request.POST['brands'])[0]
            new_car.ctitle=request.POST['model']
            new_car.regist_date=request.POST['regist_date']
            new_car.engineno=request.POST['engineNo']
            new_car.mileage=request.POST['mileage']
            new_car.maintenance_record=request.POST['isService']
            new_car.price=request.POST['price']
            new_car.extractprice=int(new_car.price)*0.02+int(new_car.price)
            new_car.newprice=request.POST['newprice']
            new_car.picture=request.FILES['pic']
            new_car.formalities=request.POST['formalities']
            new_car.debt=request.POST['isDebt']
            new_car.promise=request.POST['promise']
            new_car.serbran=brand
            new_car.user=new_user
            new_car.save()
        except ObjectDoesNotExist as e:
            return HttpResponse(e)
        return HttpResponseRedirect('/')

def person_info(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        orders = Orders.objects.filter(buy_user=user_id).order_by('-id')
        user = Users.objects.get(id=user_id)
        # 查询当前登录用户所卖的车
        car = Carinfo.objects.filter(user_id=user_id, ispurchase=0, isdelete=0)
        # 查询当前用户的最近浏览记录
        rec_view_list = []
        if request.COOKIES.get('Recently_Viewed', ''):
            cookie_car = request.COOKIES.get('Recently_Viewed', '')
            car_id = cookie_car.split(',')
            for id in car_id:
                rec_view_list.append(Carinfo.objects.get(id=id))
            print(rec_view_list)
        return render(request, 'user-info.html', {'orders': locals()})
    else:
        return redirect('login')
