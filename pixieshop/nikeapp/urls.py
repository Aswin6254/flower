from . import views
from django.urls import path
app_name='nikeapp'
urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('booking', views.booking, name='booking'),
    path('finish', views.finish, name='finish'),

]