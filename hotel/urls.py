from django.conf.urls import patterns, include, url
from django.contrib import admin
from administracion.views import AddFacturaView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hotel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^factura/$', AddFacturaView.as_view(), name='crear_factura'),
    url(r'^admin/', include(admin.site.urls)),
)
