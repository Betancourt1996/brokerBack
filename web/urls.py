
from django.urls import path, include
from . import views

from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
app_name = "web"

urlpatterns = [
    #path('admin/', admin.site.urls),


    path('', views.index, name = "index"),
    path('compania/', views.CompaniaList.as_view(),name="companialist"),
    path('compania/<int:pk>/', views.CampaniaDetail.as_view(),name="campaniadetails"),
    #path('api/', views.index, name = ""),
    #path('home/', views.index, name = "home"),
]
urlpatterns = format_suffix_patterns(urlpatterns)