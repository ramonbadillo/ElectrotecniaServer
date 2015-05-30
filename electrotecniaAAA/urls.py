<<<<<<< HEAD
"""electrotecnia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from records.views import RecordViewSet
from records.views import UserViewSet
from devices.views import DeviceViewSet



router = routers.DefaultRouter()
router.register(r'records',RecordViewSet)
router.register(r'devices',DeviceViewSet)
router.register(r'users',UserViewSet)



urlpatterns = [
    url(r'^$', 'records.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
=======
from django.conf.urls import patterns,include, url
from django.contrib import admin
from rest_framework import routers
from registrys.views import RegistryViewSet
from gadgets.views import GadgetViewSet
from devices.views import DeviceViewSet

router = routers.DefaultRouter()
router.register(r'registrys',RegistryViewSet)
router.register(r'gadgets',GadgetViewSet)
router.register(r'devices',DeviceViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'electrotecnia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^gadgets/(?P<maca>[\w\-]+)/','gadgets.views.gadgetDashboard',name='Dashboard'),
    #url(r'^signup/', 'userprofiles.views.signup',name='registrarse'),
    #url(r'^signin/', 'userprofiles.views.signin',name='entrar')
)
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
