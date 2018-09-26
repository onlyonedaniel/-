from django.conf.urls import url

from userinfo import views

urlpatterns=[
    url(r'login/',views.login,name='login'),
    url(r'logout/',views.logout,name='logout'),
    url(r'register/',views.register,name='register'),
    url(r'buyinfo/',views.buyinfo,name='buyinfo'),
    url(r'infomes_in/',views.infomes_in,name='infomes'),
    url(r'person_info/',views.person_info,name='personinfo')
]
