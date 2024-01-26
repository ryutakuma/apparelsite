from django.conf.urls import include
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.result),
    path('result', views.result),
    # path('1', views.man),
    # path('2', views.woman),
]