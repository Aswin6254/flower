from . import views
from django.urls import path
app_name='pixieshopappapp'
urlpatterns = [

    path('', views.index, name='index'),


]