from django.conf.urls import include
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('result', views.index),
    # path('1', views.man),
    # path('2', views.woman),
]