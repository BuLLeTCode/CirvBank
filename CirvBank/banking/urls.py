from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
     url(r'^$', views.home),
     url(r'^accounts/login/$', views.user_login, name="user_login"),
     url(r'^bank/$', views.bank, name="bank"),
     url('^logout/', views.user_logout, name="logout")
]
