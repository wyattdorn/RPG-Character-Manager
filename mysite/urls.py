from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    #path('charactermanager/', include('charactermanager.urls')),
    path('charactermanager/', include('charactermanager.urls')),
    path('admin/', admin.site.urls),
]
