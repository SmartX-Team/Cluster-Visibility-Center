from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.api_main),
    url(r'^testapi$', views.test_api),
    url(r'^all$', views.total_record),

    url(r'^country_code$', views.country_code_stat),
    url(r'^country_code/(?P<code>[A-Z]{2})/$', views.country_code_count),

    url(r'^comm/$', views.comm_stat),
    url(r'^comm/(?P<comm>[a-zA-Z]*)/$', views.comm_count),

    url(r'^dest/$', views.dest_ip_stat),
    url(r'^dest/(?P<dest>(\d{1,3}.){3}\d{1,3})/', views.dest_ip_count),

    url(r'^source/$', views.source_ip_stat),
    url(r'^source/(?P<dest>(\d{1,3}.){3}\d{1,3})/', views.source_ip_count),

    url(r'^onosbuild2017/$', views.onosbuild2017),
    # url(r'^onosbuild2017_simple/$', views.onosbuild2017_simple),
]
