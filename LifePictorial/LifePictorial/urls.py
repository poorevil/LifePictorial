from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView

from django.contrib.auth.views import login, logout

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) 

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
    (r'^admin$', 'admin.views.welcome'),
    (r'^admin/apps_manager_remove$', 'admin.views.apps_manager_remove'),
    (r'^admin/ads_manager$', 'admin.views.ads_manager'),
    (r'^admin/ads_manager_remove$', 'admin.views.ads_manager_remove'),
    (r'^admin/taoke_manager$', 'admin.views.taoke_manager'),
    (r'^admin/taoke_manager_remove$', 'admin.views.taoke_manager_remove'),
    (r'^admin/taokeapi_manager$', 'admin.views.taokeapi_manager'),
    (r'^admin/taokeapi_manager_remove$', 'admin.views.taokeapi_manager_remove'),
    (r'^admin/error_page$', 'admin.views.error_page'),
    (r'^admin/taokeitem_manager$', 'admin.views.taokeitem_manager'),
    (r'^admin/taokeitem_manager_sort$', 'admin.views.taokeitem_manager_sort'),
    (r'^admin/taokeitem_manager_update_order/(?P<appcode>[\w\d]{0,20})/$', 'admin.views.taokeitem_manager_update_order'),
    (r'^admin/taokeitem_manager_fetch_item_detail/(?P<num_iid>[\w\d]{0,20})/$', 'admin.views.taokeitem_manager_fetch_item_detail'),
    (r'^admin/taokeitem_manager_add_item$', 'admin.views.taokeitem_manager_add_item'),
    (r'^admin/albunm_manager_add_albunm$', 'admin.views.albunm_manager_add_albunm'),
    (r'^admin/albunm_manager$', 'admin.views.albunm_manager'),
    (r'^admin/albunm_manager_sort$', 'admin.views.albunm_manager_sort'),
    (r'^admin/albunm_manager_update_order/(?P<appcode>[\w\d]{0,20})/$', 'admin.views.albunm_manager_update_order'),
    (r'^admin/taokeitem_manager_get_picdetail$', 'admin.views.taokeitem_manager_get_picdetail'),
    (r'^admin/taokeitem_manager_update_detail$', 'admin.views.taokeitem_manager_update_detail'),
    
    
    
    
    (r'^interface/ad$', 'interface.views.ad_interface'),
    (r'^interface/recommend_album$', 'interface.views.recommend_album'),
    (r'^interface/picwaterflow$', 'interface.views.picwaterflow'),
    (r'^interface/picdetail$', 'interface.views.picdetail'),
    
    (r'^interface/picdetail_v2$', 'interface.views.picdetail_v2'),
    (r'^interface/picdetail_album_pagination$', 'interface.views.picdetail_album_pagination'),
    (r'^interface/runtime_param$', 'interface.views.runtime_param'),
    
    (r'^(?P<path>.*)$', 'django.views.static.serve'
     ,{'document_root': PROJECT_PATH+'/LifePictorial/static', 'show_indexes': False}),
    
)

#if settings.DEBUG:  
urlpatterns += staticfiles_urlpatterns() 
