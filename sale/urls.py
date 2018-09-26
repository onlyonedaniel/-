from django.conf.urls import url
from sale import views
urlpatterns=[
    #当访问路径是/sale/detail的时候
    url(r'^detail/',views.detail,name='detail'),
    url(r'^price/',views.price,name='price'),
]