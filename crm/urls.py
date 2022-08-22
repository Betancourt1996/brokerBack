
from django.urls import path, include
from . import views

from django.contrib import admin

app_name = "crm"

urlpatterns = [
    #path('admin/', admin.site.urls),


    path('', views.index, name = "home"),
    path('api/', views.index, name = "home"),
    #path('home/', views.index, name = "home"),
]
