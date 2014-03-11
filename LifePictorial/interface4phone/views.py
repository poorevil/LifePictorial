#-*- coding:UTF-8 -*-

import json

from admin.models import Adver,App,PicDetail,Categoary,Albunm
from django.http.response import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def albunmlistForMainView(request):
    ''' 首页图集列表 '''
    
    jsonstr = '[]'
    
    try:
        '''分页'''
        currpage = request.GET.get('currpage',1)
        appidStr = request.GET.get('appid','')
        if len(appidStr) > 0:
            appid = int(appidStr)
            
            app = App.objects.get(id=appid)
            categoary = app.categoary
            
            if categoary is not None:
                albunm_list = Albunm.objects.filter(categoary=app.categoary,state=1).order_by('-custom_tag','order','-last_add_time')
                paginator = Paginator(albunm_list, 25)
                
                try:
                    contacts = paginator.page(currpage)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    contacts = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    contacts = paginator.page(paginator.num_pages)
            
#                 https://docs.djangoproject.com/en/dev/topics/pagination/
#                     >>> objects = ['john', 'paul', 'george', 'ringo']
#                     >>> p = Paginator(objects, 2)
#                     >>> p.count
#                     4
#                     >>> p.num_pages
#                     2
#                     >>> p.page_range
#                     [1, 2]
#                     
#                     >>> page1 = p.page(1)
#                     >>> page1
#                     <Page 1 of 2>
#                     >>> page1.object_list
#                     ['john', 'paul']


                

                jsonstr = json.dumps(contacts.object_list, default=Albunm.serialize)

#             jsonstr = json.dumps(ad_list, default=Adver.serialize)
    except:
        pass
    
    return HttpResponse(jsonstr, content_type="application/json")