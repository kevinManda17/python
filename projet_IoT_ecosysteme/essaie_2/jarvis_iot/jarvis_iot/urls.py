from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # Routes des applications
    path('ml/', include('ml.urls')),
    path('expert/', include('expert.urls')),
    path('iot/', include('iot.urls')),
    path('agents/', include('agents.urls')),
    path('users/', include('users.urls')),
]
