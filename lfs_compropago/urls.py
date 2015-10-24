from django.conf.urls.defaults import *

from . import views

urlpatterns = [
    url(r'^status/(?P<tx_id>[0-9]+)$', views.status_view, name='compropago_instrucciones'),
    url(r'^webhook/$', views.web_hook_view, name='compropago_webhook'),
]
