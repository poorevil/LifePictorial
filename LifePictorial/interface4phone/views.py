#-*- coding:UTF-8 -*-

import json

from admin.models import Adver,App,PicDetail,Categoary,Albunm
from django.http.response import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def albunmlistForMainView(request):
    ''' 首页图集列表 '''
    
    jsonstr = '{"result_code": 500}'
    
#    {
#    "total_count": 3383,
#    "albunm_items": [
#        {
#            "picdetail_list": [
#                {
#                    "albunm_id": "4504031029",
#                    "user_id": "琉光易彩",
#                    "description": "高贵英伦风简约气质宝宝外套,很新颖时尚哦,让你的宝宝潮气十足~",
#                    "taoke_price": "279",
#                    "pid": "6851009619",
#                    "root_cate_id": 0,
#                    "height": 800,
#                    "width": 704,
#                    "cate_id": 9,
#                    "custom_tag": 0,
#                    "time": "2014-03-11 15:20:03",
#                    "taoke_title": "",
#                    "pic_path": "http://img01.taobaocdn.com/bao/uploaded/i1/11728034934992803/T1aIX7FrNuXXXXXXXX_!!1099841728-0-pix.jpg",
#                    "taoke_url": null,
#                    "albunm_name": "小美妞可爱装...",
#                    "taoke_num_iid": "36914334247"
#                },
#                ...
#            ],
#            "last_add_time": "2014-03-11 15:20:03",
#            "custom_tag": 0,
#            "pic_amount": 8,
#            "albunm_name": "小美妞可爱装...",
#            "id": "4504031029"
#         },
#         ...
#    ],
#    "result_code": 200
#    }
    
    try:
        '''分页'''
        currpage = request.GET.get('currpage',1)
        appidStr = request.GET.get('appid','')
        if len(appidStr) > 0:
            appid = int(appidStr)
            
            app = App.objects.get(id=appid)
            categoary = app.categoary
            
            if categoary is not None:
                albunm_list = Albunm.objects.filter(categoary=app.categoary,state=1,pic_amount__gt=0).order_by('-custom_tag','order','-last_add_time')
                paginator = Paginator(albunm_list, 10)
                
                try:
                    albunms = paginator.page(currpage)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    albunms = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    albunms = paginator.page(paginator.num_pages)
            
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
    
                ''' 返回的结果集 '''
                resultDict = {}
                resultDict["result_code"]=200
                resultDict["total_count"]=paginator.count
                albunmDictList = []
                for albunmObj in albunms.object_list:
                    ''' 获取图集最近6张图片 '''
                    picDetailList = list(PicDetail.objects.filter(albunm=albunmObj,state=1)
                                         .order_by('-custom_tag','order','-time')[:6])
                    albunmDict = Albunm.serialize(albunmObj)
                    picDetailDictList = []
                    for picDetailObj in picDetailList:
                        picDetailDictList.append(PicDetail.serialize(picDetailObj))
                    albunmDict["picdetail_list"] = picDetailDictList
                    
                    albunmDictList.append(albunmDict)
                
                resultDict["albunm_items"]=albunmDictList
    
                jsonstr = json.dumps(resultDict)

    except Exception,e:
#        print e
        pass
    
    return HttpResponse(jsonstr, content_type="application/json")

def picDetailList(request):
    ''' 根据图集id获取所属图片 '''
    jsonstr = '{"result_code": 500}'
    
    try:
        '''分页'''
        currpage = request.GET.get('currpage',1)
        albunmid = request.GET.get('albunmid','')
        albunmObj = Albunm.objects.get(id=albunmid)
            
        if albunmObj is not None:
            picDetailList = PicDetail.objects.filter(albunm=albunmObj,state=1).order_by('-custom_tag','order','-time')
            paginator = Paginator(picDetailList, 10)
            try:
                picDetails = paginator.page(currpage)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                picDetails = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                picDetails = paginator.page(paginator.num_pages)
            
            resultDict={}
            resultDict["result_code"]=200
            resultDict["total_count"]=paginator.count
            
            picDetailDictList=[]
            for picDetailObj in picDetails.object_list:
                
                picDetailDictList.append(PicDetail.serialize(picDetailObj))
                
            resultDict["picDetail_items"]=picDetailDictList
            jsonstr = json.dumps(resultDict)
            
    except:
        pass
    
    return HttpResponse(jsonstr, content_type="application/json")

def newestPicDetailList(request):
    ''' 获取最新图片 '''
    jsonstr = '{"result_code": 500}'
    
    try:
        '''分页'''
        currpage = request.GET.get('currpage',1)
        appidStr = request.GET.get('appid','')
        if len(appidStr) > 0:
            appid = int(appidStr)
            
            app = App.objects.get(id=appid)
            categoaryObj = app.categoary
            
            if categoaryObj is not None:
                picDetailList = PicDetail.objects.filter(categoary=categoaryObj,state=1).order_by('-custom_tag','order','-time')
                
                paginator = Paginator(picDetailList, 10)
                try:
                    picDetails = paginator.page(currpage)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    picDetails = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    picDetails = paginator.page(paginator.num_pages)
                
                resultDict={}
                resultDict["result_code"]=200
                resultDict["total_count"]=paginator.count
                
                picDetailDictList=[]
                for picDetailObj in picDetails.object_list:
                    pidDetailDict = PicDetail.serialize(picDetailObj)
                    ''' 所属图集信息 '''
                    ownerAlbunmDict = Albunm.serialize(picDetailObj.albunm)
                    pidDetailDict["ownerAlbunm"] = ownerAlbunmDict
                    
                    picDetailDictList.append(pidDetailDict)
                    
                resultDict["picDetail_items"]=picDetailDictList
                jsonstr = json.dumps(resultDict)
    
    except:
        pass
    
    return HttpResponse(jsonstr, content_type="application/json")

    

