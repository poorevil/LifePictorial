#-*- coding:UTF-8 -*-

from django import forms
from admin.models import App,TaokeAccount,TaokeAccount,TaobaoApiDetail,Categoary,Albunm
 
 
class AppsManagerEditForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AppsManagerEditForm, self).__init__(*args, **kwargs)
        ''' 更新select ''' 
        self.fields["taobaoApiDetail"].choices = (tuple([p.id, p.appKey]) for p in TaobaoApiDetail.objects.order_by('-id'))
        self.fields["taokeAccount"].choices = (tuple([p.id, p.taokeName]) for p in TaokeAccount.objects.order_by('-id'))
    
    name                     = forms.CharField(label='软件名称',max_length=50)
    detail                   = forms.CharField(label='简介',max_length=100,required=False,widget=forms.Textarea)    
    taokeAccount             = forms.ChoiceField(label='淘客账号',widget=forms.Select
                                        ,choices=tuple(tuple([p.id, p.taokeName]) for p in TaokeAccount.objects.order_by('-id'))) 
    taobaoApiDetail          = forms.ChoiceField(label='淘客api接口',widget=forms.Select
                                        ,choices=tuple(tuple([p.id, p.appKey]) for p in TaobaoApiDetail.objects.order_by('-id'))) 
    
    
class AdverManagerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AdverManagerForm, self).__init__(*args, **kwargs)
        ''' 更新select ''' 
        self.fields["app"].choices = (tuple(tuple([p.id, p.name]) for p in App.objects.order_by('-id')))
    
    
    title           = forms.CharField(label='广告名称',max_length=50)
    picUrl          = forms.CharField(label='图片地址',max_length=200)
    ''' 广告类型，1：网页url，一般为淘宝网页，2：宝贝链接，一般用客户端UI展现 '''
    adType          = forms.ChoiceField(label='广告类型',widget=forms.Select
                                        ,choices=((1,'非淘客'),(0,'淘客')))
                                           
    ''' 对应adType '''
    adIdentifier    = forms.CharField(label='产品地址',max_length=200)   
    ''' 排序权重 '''   
    order           = forms.IntegerField(label='广告排序',min_value=0)
    ''' 对应软件 '''
    app             = forms.ChoiceField(label='所属软件',widget=forms.Select
                                        ,choices=tuple(tuple([p.id, p.name]) for p in App.objects.order_by('-id'))) 
    
class TaobaoApiDetailForm(forms.Form):
    appKey          = forms.CharField(label='app key',max_length=100)         #appkey
    appSecret       = forms.CharField(label='app secret',max_length=150)      #appsecret
    
    
class TaokeAccountForm(forms.Form):
    taokeName     = forms.CharField(label='淘客账号名',max_length=100)                                           #name
    detail        = forms.CharField(label='描述',max_length=150,required=False,widget=forms.Textarea)      #detail
    
class TaokeItemAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TaokeItemAddForm, self).__init__(*args, **kwargs)
        ''' 更新select ''' 
        self.fields["albunm_id"].choices = (tuple([p.id, p.albunm_name]) for p in (Albunm.objects.order_by('-last_add_time')[:20]))
    
    num_iid         = forms.CharField(label='宝贝id',max_length=50)  
    pic_path        = forms.URLField(label='宝贝图片地址',max_length=500)  
    taoke_title     = forms.CharField(label='宝贝名称',max_length=200) 
    taoke_price     = forms.CharField(label='宝贝价格',max_length=200) 
    pic_desc        = forms.CharField(label='宝贝描述',required=False,max_length=500) 
    taoke_url       = forms.URLField(label='宝贝详情地址',max_length=500) 
    categoary_id    = forms.ChoiceField(label='所属分类',widget=forms.Select
                                        ,choices=tuple(tuple([p.id, p.title]) for p in Categoary.objects.order_by('id')))  
    albunm_id       = forms.ChoiceField(label='所属图集',widget=forms.Select
                                        ,choices=tuple(tuple([p.id, p.albunm_name]) for p in (Albunm.objects.order_by('-last_add_time')[:20]))) 
    
class AlbunmAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AlbunmAddForm, self).__init__(*args, **kwargs)
        ''' 更新select ''' 
        self.fields["categoary_id"].choices = tuple(tuple([p.id, p.title]) for p in Categoary.objects.order_by('id'))
    
    albunm_name     = forms.CharField(label='图集名称',max_length=50)  
    categoary_id    = forms.ChoiceField(label='所属分类',widget=forms.Select
                                        ,choices=tuple(tuple([p.id, p.title]) for p in Categoary.objects.order_by('id')))  
    