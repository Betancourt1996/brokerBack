
from django.contrib import admin
from django.urls import path, include

urlpatterns = [ 

    path('crm/', include('crm.urls')),
    path('web/', include('web.urls')),
    path('movil/', include('movil.urls')),
    #Modo Adminstrador
    path('admin/', admin.site.urls),
]
