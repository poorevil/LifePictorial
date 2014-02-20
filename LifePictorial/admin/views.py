#-*- coding:UTF-8 -*-

from django.shortcuts import render_to_response
#from django.contrib import auth
from admin.models import App,Adver,TaokeAccount,TaobaoApiDetail,PicDetail,Albunm,Categoary
from admin.forms import AppsManagerEditForm , AdverManagerForm,TaobaoApiDetailForm,TaokeAccountForm,TaokeItemAddForm,AlbunmAddForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import json,time,datetime

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
    albunm_id = request.GET.get('albunm_id','')
    
    albunmObj = None
    try:
        albunmObj = Albunm.objects.get(id=albunm_id)
    except Exception,e:
        pass
    
    if albunmObj is None:
        return HttpResponseRedirect('/admin/error_page')
    
    if len(appcode) >0:
        if request.method == 'POST' :
            idArray = request.POST.getlist("ids")
            oper = request.POST.get("oper")         #操作类型，submit:上架 down:下架 del:删除
            print idArray
            
            if cmp(oper,"submit") == 0 :
                for idStr in idArray:
                    picDetail = PicDetail.objects.get(id=idStr)
                    picDetail.state = 1
                    picDetail.save()
            elif cmp(oper,"down") == 0 :
                for idStr in idArray:
                    picDetail = PicDetail.objects.get(id=idStr)
                    picDetail.state = 0
                    picDetail.save()
            elif cmp(oper,"del") == 0 :
                for idStr in idArray:
                    picDetail = PicDetail.objects.get(id=idStr)
                    picDetail.delete()
                
                albunmObj.pic_amount -= len(idArray)
                albunmObj.save()
            else:
                return HttpResponseRedirect('/admin/error_page')
            
            return HttpResponseRedirect('/admin/taokeitem_manager?appcode=%s&albunm_id=%s'%(appcode,albunm_id))
        else:
            customItemList = list(PicDetail.objects.filter(albunm=albunmObj).order_by('-custom_tag','order'))
            dict = {'appcode':appcode,'customItemList':customItemList,'albunm':albunmObj}
            return render_to_response('admin/templates/taokeitem_manager.html',dict)
        
    else:
        return HttpResponseRedirect('/admin/error_page')

@login_required(login_url='/admin/login')
def taokeitem_manager_sort(request):
    ''' 用于添加淘客url '''
    appcode = request.GET.get('appcode','')
    albunmId = request.GET.get('albunm_id','')
    
    albunmObj = None
    try:
        albunmObj = Albunm.objects.get(id=albunmId)
    except Exception,e:
        print e
        pass
        
    if albunmObj is None:
        return HttpResponseRedirect('/admin/error_page')
    
    if len(appcode) >0:
        customItemList = list(PicDetail.objects.filter(albunm=albunmObj).order_by('-custom_tag','order'))
        dict = {'appcode':appcode,'customItemList':customItemList,'albunm':albunmObj}
        
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
    appcode = request.GET.get('appcode','')
    albunmId = request.GET.get('albunm_id','')
    
    albunmObj = None
    try:
        albunmObj = Albunm.objects.get(id=albunmId)
    except Exception,e:
        print e
        pass
        
    if albunmObj is None:
        return HttpResponseRedirect('/admin/error_page')
    
    if request.method == 'POST' :
        form = TaokeItemAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
#             albunm = Albunm.objects.get(id=cd['albunm_id'])
#             if albunm is not None:
            picDetail = PicDetail(pic_path=cd['pic_path'],
                                  pid=time.time(),
                                  categoary=albunmObj,
                                  taoke_num_iid=cd['num_iid'],
                                  taoke_title=cd['taoke_title'],
                                  taoke_price=cd['taoke_price'],
                                  pic_desc=cd['pic_desc'],
                                  taoke_url=cd['taoke_url'],
                                  custom_tag=1,
                                  albunm_id=cd['albunm_id'],
                                  order=0)
            picDetail.save()
            
            albunmObj.pic_amount += 1
            albunmObj.last_add_time = datetime.datetime.today()
            albunmObj.save()
             
            return HttpResponseRedirect('/admin/taokeitem_manager_add_item?appcode=%s&albunm_id=%s'%(appcode,albunmId))
    else:
        form = TaokeItemAddForm()
    
    dict = {'appcode':appcode,'form':form,'albunmId':albunmId}
    
    return render_to_response('admin/templates/taokeitem_manager_fetch_item.html',dict)
    
@login_required(login_url='/admin/login')
def taokeitem_manager_fetch_item_detail(request,num_iid):
    ''' 抓取宝贝信息 '''
    req=top.api.TbkItemsDetailGetRequest()
    req.fields="num_iid,seller_id,nick,title,price,volume,pic_url,item_url,shop_url"
    req.num_iids=num_iid
    
    try:
        f= req.getResponse()
        f['result_code']=208
#         print(f)
    
        return HttpResponse(json.dumps(f), content_type="application/json")
    
    except Exception,e:
        print(e)
    
    return HttpResponse("{'result_code':400}")

def albunm_manager_add_albunm(request):
    '''添加图集'''
    appcode = request.GET.get('appcode','')
    
    app = App.objects.get(id=appcode)
    if app is None:
        return HttpResponseRedirect('/admin/error_page')
    
    albunm_nameStr = request.POST.get("albunm_name")
    
    albunm = Albunm()
    albunm.id               = time.time()
    albunm.albunm_name      = albunm_nameStr
    albunm.pic_amount       = 0
    albunm.order            = 99999
    albunm.state            = 0
    albunm.categoary        = app.categoary
    albunm.custom_tag       = 1
    
    albunm.save()
    
    return HttpResponse('''{"result_code":200}''', content_type="application/json")


@login_required(login_url='/admin/login')
def albunm_manager(request):
    ''' 用于图集管理 '''
    
    '''分页'''
    currpage = request.GET.get('currpage',0)
    
    appcode = request.GET.get('appcode','')
    if len(appcode) >0:
        app = None
        try:
            app = App.objects.get(id=appcode)
        except Exception,e:
            print e
            pass
        
        if app is None:
            return HttpResponseRedirect('/admin/error_page')
        
        if request.method == 'POST' :
            idArray = request.POST.getlist("ids")
            oper = request.POST.get("oper")         #操作类型，submit:上架 down:下架 del:删除
#             print idArray
             
            if cmp(oper,"submit") == 0 :
                for idStr in idArray:
                    albunm = Albunm.objects.get(id=idStr)
                    albunm.state = 1
                    albunm.save()
            elif cmp(oper,"down") == 0 :
                for idStr in idArray:
                    albunm = Albunm.objects.get(id=idStr)
                    albunm.state = 0
                    albunm.save()
            elif cmp(oper,"del") == 0 :
                for idStr in idArray:
                    albunm = Albunm.objects.get(id=idStr)
                    albunm.delete()
            else:
                return HttpResponseRedirect('/admin/error_page')
             
            return HttpResponseRedirect('/admin/albunm_manager?appcode=%s'%appcode)
        else:
            albunmList = list(Albunm.objects.filter(categoary=app.categoary).order_by('-custom_tag','order','-last_add_time')[:20])
            totalAmount = Albunm.objects.filter(categoary=app.categoary).count()
            dict = {'appcode':appcode,'albunmList':albunmList,'totalAmount':totalAmount,'currpage':currpage}
            return render_to_response('admin/templates/albunm_manager.html',dict)
        
    else:
        return HttpResponseRedirect('/admin/error_page')
    
@login_required(login_url='/admin/login')
def albunm_manager_sort(request):
    ''' 用于albunm排序 '''
    appcode = request.GET.get('appcode','')
    if len(appcode) >0:
        app = None
        try:
            app = App.objects.get(id=appcode)
        except Exception,e:
            pass
        
        if app is None:
            return HttpResponseRedirect('/admin/error_page')
    
        albunmList = list(Albunm.objects.filter(categoary=app.categoary,custom_tag=1,state=1).order_by('order'))
        
        dict = {'appcode':appcode,'customItemList':albunmList}
        
        return render_to_response('admin/templates/albunm_sort.html',dict)
    else:
        return HttpResponseRedirect('/admin/error_page')
    
@login_required(login_url='/admin/login')
def albunm_manager_update_order(request,appcode):
    ''' 修改排序 '''
    #[{"item_id":"3","currOrder":0},{"item_id":"2","currOrder":2},{"item_id":"5","currOrder":3}]
    jsonStr = request.POST.get('jsonStr','');
    
    jsonArray = json.loads(jsonStr)
    
    for dict in jsonArray:
        albunm = Albunm.objects.get(id=dict["item_id"])
        albunm.order = dict["currOrder"]
        albunm.save()
    
    return HttpResponse("ok")




