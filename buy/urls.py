from django.conf.urls import url
from buy import views
urlpatterns=[
    url(r'brandlist/$',views.brandlist,name='brandlist'),
    url(r'addorder/$',views.add_order,name='addorder'),
    url(r'delcart/$',views.del_order,name='delcart'),
    url(r'confirmbuy/$',views.confirm_buy,name='confirmbuy'),
]