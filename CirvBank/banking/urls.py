from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
     #url(r'^$', views.home),
     url(r'^accounts/login/$', views.user_login, name="user_login"),
	 url(r'^$', views.user_login, name="user_login"),
     url(r'^bank/$', views.bank, name="bank"),
     url(r'^transactions/$', views.transactions, name="transactions"),
     url(r'^info/$', views.user_info, name="user_info"),
     url(r'^logout/', views.user_logout, name="logout"),
     url(r'^banklink_template/', views.banklink_template, name="banklink_template"),

     # pienem linku : "/banklink?acc=BLAHBLASDFA&sum=12314"
     url(r'^banklink/', views.banklink_login, name="banklink_login")
]
