#-*- coding:UTF-8 -*-

from django.shortcuts import render_to_response
#from django.contrib import auth
from admin.models import App,Adver,TaokeAccount,TaobaoApiDetail,PicDetail
from admin.forms import AppsManagerEditForm , AdverManagerForm,TaobaoApiDetailForm,TaokeAccountForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import json

import top.api

from django.http.response import HttpResponse

'''
这边可以设置一个默认的appkey和secret，当然也可以不设置
注意：默认的只需要设置一次就可以了
'''
'''
可以在运行期替换掉默认的appkey和secret的设置
a.set_app_info(top.appinfo("appkey","*******"))
'''
# top.setDefaultAppInfo("21589744", "29029858003d0142d25aeed24c6e5e5b")
top.setDefaultAppInfo("21125417", "2b4fc27525fd9a225cdedcbb0a6862a7")
#def login(request):
#    
#    username = request.POST.get('username','')
#    pwd = request.POST.get('password','')
#    
#    user = auth.authenticate(username=username,password=pwd)
#    
#    if user is not None and user.is_active:
#        # Correct password, and the user is marked "active"
#        auth.login(request, user)
#        # Redirect to a success page.
#        return HttpResponseRedirect("/admin/welcome")
#    else:
#        # Show an error page
#        return HttpResponseRedirect("/admin/")
# 

#   重置用户密码
#from django.contrib.auth.models import User
#def resetUser(request):
#    user = User.objects.get(username='poorevil')
#    user.set_password('akbca19')
#    user.save()
#
#    return HttpResponse("ok", content_type="application/json")


@login_required(login_url='/admin/login')
def welcome(request):
    app_list = App.objects.order_by('-id')
    return render_to_response('admin/templates/admin_welcome.html',{'app_list':app_list})


@login_required(login_url='/admin/login')
def apps_manager(request):

    form = None
    if request.method == 'POST' :
        form = AppsManagerEditForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            app = App(name=cd['name'],detail=cd['detail']
                      ,taokeAccount=TaokeAccount(id=cd['taokeAccount'])
                      ,taobaoApiDetail=TaobaoApiDetail(id=cd['taobaoApiDetail']))
            app.save()
            
            return HttpResponseRedirect('/admin/apps_manager')

    app_list = App.objects.order_by('id')
    if form is None:
        form = AppsManagerEditForm()
    
    dict = {'app_list':app_list,'form':form}
    return render_to_response('admin/templates/admin_apps_manager.html',dict)

''' 删除app '''
@login_required(login_url='/admin/login')
def apps_manager_remove(request):
    
    appId = request.POST.get('id','')
    app = App.objects.get(id=int(appId))
    app.delete()
    
    return HttpResponseRedirect('/admin/apps_manager')

@login_required(login_url='/admin/login')
def ads_manager(request):
    
    form = None
    appcode = request.GET.get('appcode','')
    
    if len(appcode) >0:
        adver_list = Adver.objects.filter(app=App(id=appcode)).order_by('order')
        
        if request.method == 'POST' :
            form = AdverManagerForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                adver = Adver(title=cd['title'],
                              picUrl=cd['picUrl'],
                              adType=cd['adType'],
                              adIdentifier=cd['adIdentifier'],
                              order=cd['order'],
                              app=App.objects.get(id=cd['app']))
                
                adver.save()
                
                return HttpResponseRedirect('/admin/ads_manager?appcode=%s'%appcode)
        
        if form is None:
            form = AdverManagerForm(initial={'app': appcode})
        
        dict = {'appcode':appcode,'adver_list':adver_list,'form':form}
        
        return render_to_response('admin/templates/admin_advert_manager.html',dict)
    
    else:
        return HttpResponseRedirect('/admin/error_page')
    
    
def ads_manager_remove(request):
    
    appcode = request.GET.get('appcode','')
    
    id = request.POST.get('id','')
    
    if id is not None and id != '' :
        adver = Adver.objects.get(id=int(id))
        adver.delete()
    
    return HttpResponseRedirect('/admin/ads_manager?appcode=%s'%appcode)
    

def taoke_manager(request):
    ''' 淘客账号管理 '''
    form = None
    taoke_list = TaokeAccount.objects.order_by('id')
    
    if request.method == 'POST' :
        form = TaokeAccountForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            taoke = TaokeAccount(taokeName=cd['taokeName'],
                                 detail=cd['detail'])
            
            taoke.save()
            
            return HttpResponseRedirect('/admin/taoke_manager')
    
    if form is None:
        form = TaokeAccountForm()
    
    dict = {'taoke_list':taoke_list,'form':form}
    
    return render_to_response('admin/templates/admin_taoke_manager.html',dict)
    
def taoke_manager_remove(request):
    ''' 淘客账号管理--删除 '''
    taokeId = request.POST.get('id',None)
    
    if taokeId is not None:
        taoke = TaokeAccount(id=taokeId)
        taoke.delete()
        
    return HttpResponseRedirect('/admin/taoke_manager')

def taokeapi_manager(request):
    ''' 淘客api管理 '''
    form = None
    taokeapi_list = TaobaoApiDetail.objects.order_by('id')
    
    if request.method == 'POST' :
        form = TaobaoApiDetailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            taokeapi = TaobaoApiDetail(appKey=cd['appKey'],
                                       appSecret=cd['appSecret'])
            
            taokeapi.save()
            
            return HttpResponseRedirect('/admin/taokeapi_manager')
    
    if form is None:
        form = TaobaoApiDetailForm()
    
    dict = {'taokeapi_list':taokeapi_list,'form':form}
    
    return render_to_response('admin/templates/admin_taokeapi_manager.html',dict)

def taokeapi_manager_remove(request):
    ''' 淘客api管理--删除 '''
    taokeId = request.POST.get('id',None)
    
    if taokeId is not None:
        taokeapi = TaobaoApiDetail(id=taokeId)
        taokeapi.delete()
        
    return HttpResponseRedirect('/admin/taokeapi_manager')
    
def error_page(request):
    '''错误页'''
    #TODO:临时错误页
    return render_to_response('admin/templates/error_page.html')


@login_required(login_url='/admin/login')
def taokeitem_manager(request):
    ''' 用于添加淘客url '''
    
    appcode = request.GET.get('appcode','')
    
    if len(appcode) >0:
        
        
#         if request.method == 'POST' :
#             form = AdverManagerForm(request.POST)
#             if form.is_valid():
#                 cd = form.cleaned_data
#                 adver = Adver(title=cd['title'],
#                               picUrl=cd['picUrl'],
#                               adType=cd['adType'],
#                               adIdentifier=cd['adIdentifier'],
#                               order=cd['order'],
#                               app=App.objects.get(id=cd['app']))
#                  
#                 adver.save()
#                  
#                 return HttpResponseRedirect('/admin/ads_manager?appcode=%s'%appcode)
        
        customItemList = list(PicDetail.objects.filter(custom_tag=1).order_by('order'))
        
        dict = {'appcode':appcode,'customItemList':customItemList}
        
        return render_to_response('admin/templates/taokeitem_manager.html',dict)
        
    else:
        return HttpResponseRedirect('/admin/error_page')

@login_required(login_url='/admin/login')
def taokeitem_manager_sort(request):
    ''' 用于添加淘客url '''
    appcode = request.GET.get('appcode','')
    
    if len(appcode) >0:
        customItemList = list(PicDetail.objects.filter(custom_tag=1).order_by('order'))
        dict = {'appcode':appcode,'customItemList':customItemList}
        
        return render_to_response('admin/templates/taokeitem_sort.html',dict)
    else:
        return HttpResponseRedirect('/admin/error_page')
    
@login_required(login_url='/admin/login')
def taokeitem_manager_update_order(request,appcode):
    ''' 修改排序 '''
    #[{"item_id":"3","currOrder":0},{"item_id":"2","currOrder":2},{"item_id":"5","currOrder":3}]
    jsonStr = request.POST.get('jsonStr','');
    print jsonStr;
    
    jsonArray = json.loads(jsonStr)
    
    for dict in jsonArray:
        picDetail = PicDetail.objects.get(id=dict["item_id"])
        picDetail.order = dict["currOrder"]
        picDetail.save()
    
    return HttpResponse("ok")

@login_required(login_url='/admin/login')
def taokeitem_manager_add_item(request):
    ''' 添加宝贝信息 '''
    
    return render_to_response('admin/templates/taokeitem_manager_fetch_item.html')

@login_required(login_url='/admin/login')
def taokeitem_manager_fetch_item_detail(request,num_iid):
    ''' 抓取宝贝信息 '''
    
#     a = top.api.ItemGetRequest()
#     a.fields="num_iid,title"
#     a.num_iid=num_iid

    req=top.api.TbkItemsDetailGetRequest()
    req.fields="num_iid,seller_id,nick,title,price,volume,pic_url,item_url,shop_url"
    req.num_iids=num_iid
    
    try:
        f= req.getResponse()
        print(f)
        return HttpResponse(f)
    except Exception,e:
        print(e)
    
    return HttpResponse("{'result_code':400}")

