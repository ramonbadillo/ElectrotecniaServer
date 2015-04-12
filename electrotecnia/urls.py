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
)
