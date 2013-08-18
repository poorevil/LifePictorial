from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView

from django.contrib.auth.views import login, logout

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LifePictorial.views.home', name='home'),
    # url(r'^LifePictorial/', include('LifePictorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
#    (r'^admin/$',TemplateView.as_view(template_name="admin/templates/admin_login.html")),
#    (r'^admin/reset$', 'admin.views.resetUser'),

    (r'^admin/login$', 'django.contrib.auth.views.login', {'template_name': 'admin/templates/admin_login.html'}),
    (r'^admin/apps_manager$', 'admin.views.apps_manager'),
    (r'^admin/$', 'admin.views.welcome'),
    (r'^admin/apps_manager_remove$', 'admin.views.apps_manager_remove'),
    (r'^admin/ads_manager$', 'admin.views.ads_manager'),
    (r'^admin/ads_manager_remove$', 'admin.views.ads_manager_remove'),
    (r'^admin/taoke_manager$', 'admin.views.taoke_manager'),
    (r'^admin/taoke_manager_remove$', 'admin.views.taoke_manager_remove'),
    (r'^admin/taokeapi_manager$', 'admin.views.taokeapi_manager'),
    (r'^admin/taokeapi_manager_remove$', 'admin.views.taokeapi_manager_remove'),
    
    
    (r'^interface/ad$', 'interface.views.ad_interface'),
    (r'^interface/recommend_album$', 'interface.views.recommend_album'),
    (r'^interface/picwaterflow$', 'interface.views.picwaterflow'),
    (r'^interface/picdetail$', 'interface.views.picdetail'),
    
    (r'^interface/picdetail_v2$', 'interface.views.picdetail_v2'),
    (r'^interface/picdetail_album_pagination$', 'interface.views.picdetail_album_pagination'),
    (r'^interface/runtime_param$', 'interface.views.runtime_param'),
    
    
    
)

#if settings.DEBUG:  
urlpatterns += staticfiles_urlpatterns() 
