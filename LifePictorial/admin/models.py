#-*- coding:UTF-8 -*-

from django.db import models
import datetime
from json import JSONEncoder

'''
CREATE TABLE "categoary" 
("cid" VARCHAR PRIMARY KEY  NOT NULL , 
"title" VARCHAR, 
"parent_cid" VARCHAR NOT NULL  DEFAULT 0)
'''
''' 宝贝所属分类 '''
class Categoary(models.Model):
    title       = models.CharField(max_length=100)
    parent_cid  = models.ForeignKey('self', blank=True, null=True, default=0)   #指向自己的外键
    
    def __unicode__(self):
        return self.title;

'''
CREATE TABLE "pic_detail" 
("pid" VARCHAR PRIMARY KEY  NOT NULL , 
"pic_path" VARCHAR, "height" INTEGER, 
"width" INTEGER, "desc" VARCHAR, 
"cate_id" INTEGER, 
"root_cate_id" INTEGER, 
"albunm_name" VARCHAR, 
"albunm_id" VARCHAR, 
"user_id" VARCHAR, 
"time" VARCHAR, 
"taoke_num_iid" VARCHAR, 
"taoke_title" VARCHAR, 
"taoke_price" VARCHAR)
'''
''' 宝贝对象 '''
class PicDetail(models.Model,JSONEncoder):
    pid             = models.CharField(max_length=20,unique=True)   #用于排重
    pic_path        = models.CharField(max_length=500)
    width           = models.IntegerField(null=True,blank=True)
    height           = models.IntegerField(null=True,blank=True)
    categoary       = models.ForeignKey(Categoary)
    albunm_name     = models.CharField(max_length=500, blank=True, null=True)
    albunm_id       = models.CharField(max_length=50, blank=True, null=True)
    user_id         = models.CharField(max_length=50, blank=True, null=True)
    time            = models.DateTimeField(blank=True, null=True)
    taoke_num_iid   = models.CharField(max_length=50, blank=True, null=True)
    taoke_title     = models.CharField(max_length=200, blank=True, null=True)
    taoke_price     = models.CharField(max_length=50, blank=True, null=True)
    pic_desc        = models.CharField(max_length=800, blank=True, null=True)
    
    #2014-02-10 added
    taoke_url       = models.CharField(max_length=500, blank=True, null=True)   #淘客链接
    custom_tag      = models.IntegerField(null=True,blank=True)                 #手动添加标记 1，手动添加 0、空，自动添加
    order           = models.IntegerField()                                     #排序
    state           = models.IntegerField(default=1)                            #状态，1，发布 0，待发布
    
    def __unicode__(self):
        return self.pic_path;
    
    @staticmethod
    def serialize(obj):
        return {
            "pid":   obj.pid,
            "pic_path": obj.pic_path,
            "height": obj.height,
            "width": obj.width,
            "description": obj.pic_desc,
            "cate_id": obj.categoary.id,
            "root_cate_id": 0 if obj.categoary is None or obj.categoary.parent_cid is None else obj.categoary.parent_cid.id,
            "albunm_name": obj.albunm_name,
            "albunm_id": obj.albunm_id,
            "user_id": obj.user_id,
            "time": obj.time.strftime('%Y-%m-%d %H:%M:%S') if isinstance(obj.time, datetime.datetime) else None,    #obj.time,
            "taoke_num_iid": obj.taoke_num_iid,
            "taoke_title": obj.taoke_title,
            "taoke_price": obj.taoke_price,
            "taoke_url": obj.taoke_url,
            "custom_tag": obj.custom_tag
        }
    
class TaokeAccount(models.Model,JSONEncoder):
    ''' 淘客账号信息 '''
    taokeName       = models.CharField(max_length=100)                           #淘客账号名称，用于生成淘客链接
    detail          = models.CharField(max_length=150,null=True,blank=True)      #描述

    def __unicode__(self):
        return 'TaokeAccount:%s'%self.taokeName
    
    @staticmethod
    def serialize(obj):
        return {
            "taokeName": obj.taokeName,
        }
        
class TaobaoApiDetail(models.Model,JSONEncoder):
    ''' 淘宝接口信息 '''
    appKey          = models.CharField(max_length=100)      #appkey
    appSecret       = models.CharField(max_length=150)      #appsecret

    def __unicode__(self):
        return 'TaobaoApiDetail:%s'%self.appKey
    
    @staticmethod
    def serialize(obj):
        return {
            "appKey":   obj.appKey,
            "appSecret": obj.appSecret,
        }

''' 客户端对象，用于管理所有以上线app '''
class App(models.Model):
    name            = models.CharField(max_length=50)
    detail          = models.CharField(max_length=100,null=True,blank=True)
    taokeAccount    = models.ForeignKey(TaokeAccount)
    taobaoApiDetail = models.ForeignKey(TaobaoApiDetail)
    
    def __unicode__(self):
        return self.name
    
''' 软件轮播图对象 '''    
class Adver(models.Model,JSONEncoder):
    title           = models.CharField(max_length=50)
    picUrl          = models.CharField(max_length=200)
    ''' 广告类型，1：网页url，一般为淘宝网页，2：宝贝链接，一般用客户端UI展现 '''
    adType          = models.IntegerField()                 
    ''' 对应adType '''
    adIdentifier    = models.CharField(max_length=200)   
    ''' 排序权重 '''   
    order           = models.IntegerField()
    ''' 对应软件 '''
    app             = models.ForeignKey(App)
    
    def __unicode__(self):
        return self.title
    
    @staticmethod
    def serialize(obj):
        return {
            "aId":   obj.id,
            "title": obj.title,
            "picUrl": obj.picUrl,
            "adType": obj.adType,
            "adIdentifier": obj.adIdentifier,
            "order": obj.order,
            "appId": obj.app.id
        }