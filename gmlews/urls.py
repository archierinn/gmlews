"""gmlews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from restapi import views
from nodes import views
from sensors import views
""" for routers api root"""
from restapi.models import Data, Node
from rest_framework import routers
from restapi.views import DataViewSet, NodeViewSet

router = routers.DefaultRouter()

router.register(r'data', DataViewSet, 'data')

router.register(r'node', NodeViewSet, 'node')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', include('sensors.urls')),
    path('register/', include('register.urls')),
    path('nodes/', include('nodes.urls')),
    path('mainpage/', include('mainpage.urls')),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path(r'api/', include(router.urls)),
    path(r'', include('rest_framework.urls', namespace='rest_framework')),
    
]
