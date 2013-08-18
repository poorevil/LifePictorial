#-*- coding:UTF-8 -*-

import json

from admin.models import Adver,App,PicDetail,Categoary
from django.http.response import HttpResponse
from django.db import connection

import random 

def ad_interface(request):
    ''' 广告接口 '''
    
    jsonstr = '[]'
    
    try:
        appid = int(request.GET.get('appid',''))
        if appid is not None and appid != '':
            ad_list = list(Adver.objects.filter(app=App(id=int(appid))).order_by('order'))
            jsonstr = json.dumps(ad_list, default=Adver.serialize)
    except:
        pass
    
    return HttpResponse(jsonstr, content_type="application/json")

def recommend_album(request):
    '''
    图集推荐列表
    '''
    
    jsonStr='[]'
    
    try:
        pageSize = 6
        
        page = int(request.GET.get('p',0))
        cid = int(request.GET.get('cid',''))
        
        if cid is not None and cid != '':
            
            '''
            最大页数9
            '''
            if page > 30:
                page = 30
            elif page < 0:
                page = 0
            
            albumResults = list(PicDetail.objects.raw('''SELECT id, albunm_id ,albunm_name, count(*) as amount 
                        FROM admin_picdetail where categoary_id=%d group by albunm_id having count(*) > %d 
                        order by time desc limit %d offset %d '''%(int(cid),4,pageSize,page*pageSize)))
            
            resultArray = []
            for row in albumResults:
                #albunm_id ,albunm_name, count(*) as amount
                resultDict = {}
                resultDict['albunmId'] = row.albunm_id
                resultDict['albunmName'] = row.albunm_name
                
                picResults = list(PicDetail.objects.filter(albunm_id=row.albunm_id)[:pageSize])
                
                picModelArray = []
    #            pid,pic_path,height,width,description,cate_id,root_cate_id,
    #                        albunm_name,albunm_id,user_id,time,taoke_num_iid,taoke_title,taoke_price'''
                for picRow in picResults:
                    picDict = {}
                    picDict['pid'] = picRow.pid
                    picDict['pic_path'] = picRow.pic_path
                    picDict['pic_desc'] = picRow.pic_desc
                    
                    picModelArray.append(picDict)
                
                resultDict['picDetail'] = picModelArray
                
                resultArray.append(resultDict)
            
            jsonStr = json.dumps(resultArray)
            
    except :
        pass
    
    return HttpResponse(jsonStr,content_type="application/json") 

def picwaterflow(request):
    
    '''
    图片瀑布流接口
    '''
    pageSize = 20
    
    jsonStr='[]'
    
    try:
        page = int(request.GET.get('p',0))
        albumId = request.GET.get('albumId','') 
        cid = request.GET.get('cid','') 
        
        if cid is not None and cid!='':
            if len(albumId) < 8:
                albumId = None
            
            '''
            最大页数9
            '''
            if page < 0:
                page = 0
            
            albumResults = PicDetail.objects.filter(categoary=Categoary(id=cid))
            
            if albumId is not None:
                albumResults = albumResults.filter(albunm_id=albumId)
            
            albumResults = albumResults[page*pageSize:(page+1)*pageSize] 
#            dao.getPicDetailByAlbunmId(limit=pageSize,offset=page*pageSize,albunmId=albumId,cateId=cid)
            
            
            jsonStr = json.dumps(list(albumResults), default=PicDetail.serialize)
            
#            resultArray = []
#            for row in albumResults:
#                '''
#                pid,pic_path,height,width,description,cate_id,root_cate_id,
#                            albunm_name,albunm_id,user_id,time,taoke_num_iid,taoke_title,taoke_price
#                            '''
#                picDict = {}
#                picDict['pid'] = row[0]
#                picDict['pic_path'] = row[1]
#                picDict['height'] = row[2]
#                picDict['width'] = row[3]
#                picDict['description'] = row[4]
#                picDict['cate_id'] = row[5]
#                picDict['root_cate_id'] = row[6]
#                picDict['albunm_name'] = row[7]
#                picDict['albunm_id'] = row[8]
#                picDict['user_id'] = row[9]
#                picDict['time'] = row[10]
#                picDict['taoke_num_iid'] = row[11]
#                picDict['taoke_title'] = row[12]
#                picDict['taoke_price'] = row[13]
#                
#                resultArray.append(picDict)
        
    except:
        pass
    
    return HttpResponse(jsonStr,content_type="application/json") 
    
    
def picdetail(request):
    ''' 图集推荐列表 '''
    
    jsonStr='[]'
    
    try:
        '''
        {
            "picDetail": {
                "albunm_id": "22464807",
                "user_id": "862605167",
                "description": "配色简洁的魅力开衫\n.柔和自然的配色，很适合春季的氛围",
                "taoke_price": "115.00",
                "pid": "64848695",
                "root_cate_id": 0,
                "height": 220,
                "width": 220,
                "cate_id": 9,
                "time": "2013-03-19 16:58:57",
                "taoke_title": "韩国进口正品童装【部分现货】三只熊P 148590 条纹休闲开衫",
                "pic_path": "http://img04.taobaocdn.com/imgextra/i4/15167022543695582/T1XHROXppbXXXXXXXX_!!862605167-0-pix.jpg",
                "albunm_name": "帅气男宝的休闲小风度",
                "taoke_num_iid": "17418578063"
            },
            "picModelInAlbumArray": [
                {
                    "pic_path": "http://img04.taobaocdn.com/imgextra/i4/15167020618926233/T1NHdNXsdeXXXXXXXX_!!862605167-0-pix.jpg",
                    "pid": "64852851"，
                    "pic_desc": "adsfsdfdsfdsf"
                },
                {
                    "pic_path": "http://img04.taobaocdn.com/imgextra/i4/15167020625977313/T1YINOXvVbXXXXXXXX_!!862605167-0-pix.jpg",
                    "pid": "64852083",
                    "pic_desc": "adsfsdfdsfdsf"
                },
                ...
            ]
        }
        '''
        pageSize = 20
        
        pid = request.GET.get('pid',None)
        cid = request.GET.get('cid',None)
        
        if pid is None or len(pid) < 8 or cid is None:
            return HttpResponse('[]',content_type="application/json")
            
        picResult = PicDetail.objects.get(pid=pid)
    
        if picResult is None:
            return HttpResponse('[]',content_type="application/json")
        
        resultDict = {}
        resultDict['picDetail'] = picResult
        
        '''
        所属图集其他图片
        '''
        albumResult = PicDetail.objects.filter(albunm_id=picResult.albunm_id)   #dao.getPicDetailByAlbunmId(6000, 0, picDict['albunm_id'])
        picModelInAlbumArray = []
    
        ''' 当前图片在图集中的位置 '''
        currentPicIdxInAlbumArray = 0
        
        for idx,picRow in enumerate(albumResult):
            
            if cmp(picRow.pid,picResult.pid) == 0:
                currentPicIdxInAlbumArray = idx
                
            albumDict = {}
            albumDict['pid'] = picRow.pid
            albumDict['pic_path'] = picRow.pic_path
            albumDict['pic_desc'] = picRow.pic_desc
        
            picModelInAlbumArray.append(albumDict)
        
        
        if len(picModelInAlbumArray) <= 6 :
            resultDict['picModelInAlbum'] = picModelInAlbumArray
        else:
            if len(picModelInAlbumArray) - (currentPicIdxInAlbumArray+1) >= 5 :
                if currentPicIdxInAlbumArray != 0:
                    resultDict['picModelInAlbum'] = picModelInAlbumArray[currentPicIdxInAlbumArray-1:currentPicIdxInAlbumArray+5]
                else:
                    resultDict['picModelInAlbum'] = picModelInAlbumArray[0:currentPicIdxInAlbumArray+6]
            else :
                resultDict['picModelInAlbum'] = picModelInAlbumArray[len(picModelInAlbumArray)-6:len(picModelInAlbumArray)]
            
        '''
        相关推荐图集
        '''
        cursor = connection.cursor()
        cursor.execute('''SELECT count(*) as amount FROM (SELECT albunm_id FROM admin_picdetail 
                       WHERE categoary_id = %s group by albunm_id having count(*) > %s) a''',[cid,5])
        row = cursor.fetchone()
        
        offset = row[0]
        
        '''TODO:?'''
        if offset > 8:
            offset = random.randint(0,row[0]-8)
            
        cursor = connection.cursor()
        cursor.execute('''SELECT albunm_id ,albunm_name, count(*) as amount 
                        FROM admin_picdetail where categoary_id=%s group by albunm_id having count(*) > %s 
                        order by time desc limit %s offset %s ''',[cid,5,6,offset])
        #dao.getRecommendAlbumIdByMinAmount(5, 6, offset,int(cid));
        
        albumResults = cursor.fetchall()
        
        resultArray = []
        for row in albumResults:
            #albunm_id ,albunm_name, count(*) as amount
            albumDict = {}
            albumDict['albunmId'] = row[0]
            albumDict['albunmName'] = row[1]
            
            picResults = PicDetail.objects.filter(albunm_id=row[0])[:3] 
    #            dao.getPicDetailByAlbunmId(3,0,row[0])
            
            picModelArray = []
    #            pid,pic_path,height,width,description,cate_id,root_cate_id,
    #                        albunm_name,albunm_id,user_id,time,taoke_num_iid,taoke_title,taoke_price'''
            for picRow in picResults:
                pDict = {}
                pDict['pid'] = picRow.pid
                pDict['pic_path'] = picRow.pic_path
                pDict['pic_desc'] = picRow.pic_desc
                
                picModelArray.append(pDict)
            
            albumDict['picDetail'] = picModelArray
            
            resultArray.append(albumDict)
            
        resultDict['recommendAlbum'] = resultArray
    
        jsonStr = json.dumps(resultDict,default=PicDetail.serialize)
        
    
        return HttpResponse(jsonStr,content_type="application/json") 
    except:
        pass
    
    return HttpResponse(jsonStr,content_type="application/json") 

def picdetail_v2(request):
    ''' 图集推荐列表 '''
    
    jsonStr='[]'
    
    try:
        '''
        {
            "albumPageSize": 6,
            "albumPageAmount": 20,
            "currentPageNo": 3,
            "albumPicAmount": 10,
            "albumPagination": {
                "currentPage": {
                    "pageNo": 3,
                    "picArray": [
                        {
                            "taoke_price": "46.00",
                            "pid": "71263265",
                            "taoke_title": "女童T恤 2013春装新款 百搭春秋款 凸印彩色螺纹亮片向日葵上衣",
                            "pic_desc": "百搭凸印彩色螺纹亮片向日葵上衣,简单的T恤,不规则的涂鸦螺纹,采用特殊的浮雕印刷工艺, 点缀缤纷~",
                            "pic_path": "http://img02.taobaocdn.com/imgextra/i2/10912021924954413/T178afXrtdXXXXXXXX_!!705450912-0-pix.jpg",
                            "taoke_num_iid": "17596282334"
                        },
                        ...
                    ]
                },
                "nextPage": {
                    "pageNo": 4,
                    "picArray": [
                        {
                            "taoke_price": "39.90",
                            "pid": "71260699",
                            "taoke_title": "女童休闲裤 2013春装新款童装 碎花田园风长裤 韩版哈伦裤",
                            "pic_desc": "软软的针织棉小哈伦裤造型，使它成为单穿或打底都可以的针织裤，版型略松但不肥大，属于修身的裤型~",
                            "pic_path": "http://img03.taobaocdn.com/imgextra/i3/10912021924706444/T1r6efXABeXXXXXXXX_!!705450912-0-pix.jpg",
                            "taoke_num_iid": "23762232269"
                        },
                        ...
                    ]
                },
                "previousPage": {
                    "pageNo": 2,
                    "picArray": [
                        {
                            "taoke_price": "65.00",
                            "pid": "71274032",
                            "taoke_title": "女童牛仔裤 童装2013春装新款长裤 韩版儿童针织柔软弹力牛仔裤子",
                            "pic_desc": "韩版儿童针织柔软弹力牛仔裤子,深深浅浅的牛仔蓝像那次旅行看到的大海,层层递进的海水诱惑着你一点一点的靠近,呼吸自由空气放飞一种心情~",
                            "pic_path": "http://img02.taobaocdn.com/imgextra/i2/10912021926782412/T11r9gXCdcXXXXXXXX_!!705450912-0-pix.jpg",
                            "taoke_num_iid": "23162252195"
                        },
                        ...
                    ]
                }
            },
            "picDetail": {
                "albunm_id": "22805826",
                "user_id": "705450912",
                "description": "长袖韩版百搭儿童口袋字母T恤,舒适的T恤棉质,休闲随意的风格~",
                "taoke_price": "49.90",
                "pid": "71262089",
                "root_cate_id": 0,
                "height": 220,
                "width": 220,
                "cate_id": 9,
                "time": "2013-04-17 22:03:25",
                "taoke_title": "女童T恤 童装2013春装新款打底衫 长袖韩版百搭儿童口袋字母T恤",
                "pic_path": "http://img04.taobaocdn.com/imgextra/i4/10912021928242632/T1ZMWfXChfXXXXXXXX_!!705450912-0-pix.jpg",
                "albunm_name": "时尚女童装 给宝贝棉花糖般的爱",
                "taoke_num_iid": "17499494539"
            },
            "recommendAlbum": [
                {
                    "albunmId": "22579429",
                    "albunmName": "变身俏皮小公主 连衣裙美艳无敌",
                    "picDetail": [
                        {
                            "pic_desc": "春装裙子牛仔裙，纯棉蕾丝花边搭配PU皮小装饰，金属质感扣子简洁大气。PU皮腰带衬托出衣服的质感。",
                            "pic_path": "http://img04.taobaocdn.com/imgextra/i4/15576021093341606/T1zJVZXtlcXXXXXXXX_!!176835576-0-pix.jpg",
                            "pid": "67254892"
                        },
                        {
                            "pic_desc": "满满的花朵十足的田园气息，散发着一种清新自然的感觉，领口的珠子装饰很别致，甜美可爱。",
                            "pic_path": "http://img02.taobaocdn.com/imgextra/i2/15576021103924983/T1qSV0XwBaXXXXXXXX_!!176835576-0-pix.jpg",
                            "pid": "67255035"
                        },
                        {
                            "pic_desc": "无袖雪纺裙连衣裙，蕾丝与雪纺面料的拼接，时尚优雅。腰后大大的蝴蝶结，非常的甜美可爱，宛如童话里的小公主。",
                            "pic_path": "http://img03.taobaocdn.com/imgextra/i3/15576021100325097/T1Pgd1Xs0XXXXXXXXX_!!176835576-0-pix.jpg",
                            "pid": "67256001"
                        }
                    ]
                },
                ...
            ]
        }
        '''
        
        pid = request.GET.get('pid',None)
        cid = request.GET.get('cid',None)
        
        if pid is None or len(pid) < 8 or cid is None:
            return HttpResponse('[]',content_type="application/json")
        
        picResult = PicDetail.objects.get(pid=pid)
        
        if picResult is None:
            return HttpResponse('[]',content_type="application/json")
        
        resultDict = {}
        
        '''
        图片信息
        '''
        resultDict['picDetail'] = picResult
        
        '''
        所属图集其他图片
        '''
        albumPagination = {}
        
        albumResult = PicDetail.objects.filter(albunm_id=picResult.albunm_id)
    #            pid,pic_path,height,width,description,cate_id,root_cate_id,
    #                        albunm_name,albunm_id,user_id,time,taoke_num_iid,taoke_title,taoke_price'''
    
    
        ''' 图集每页显示数量 '''
        albumPageSize = 6
        resultDict['albumPageSize'] = albumPageSize
        
        ''' 图集中，图片数量 '''
        cursor = connection.cursor()
        cursor.execute('''select count(*) as amount from admin_picdetail 
                        where albunm_id = %s ''',[picResult.albunm_id])
        
        albumPicAmount = cursor.fetchone()[0]
        resultDict['albumPicAmount'] = albumPicAmount
    
        ''' 图集总页数 '''
        albumPageAmount = len(albumResult)/albumPageSize
        if len(albumResult)%albumPageSize > 0:
            albumPageAmount = albumPageAmount + 1
            
        resultDict['albumPageAmount'] = albumPageAmount
    
        ''' 当前图片在图集中的位置 '''
        currentPicIdxInAlbumArray = 0            
        for idx,picRow in enumerate(albumResult):
            if cmp(picRow.pid,picResult.pid) == 0:
                currentPicIdxInAlbumArray = idx
                break
            
        ''' 当前图片所在图集第几页 '''
        currentPageNo = currentPicIdxInAlbumArray / albumPageSize
        
        resultDict['currentPageNo'] = currentPageNo
        
        currentPage = {}
        
        currentPage['pageNo'] = currentPageNo
        currentPage['picArray'] = []
        
        ''' current '''
        for idx in range(currentPageNo * albumPageSize,(currentPageNo+1) * albumPageSize):
            
            if idx >= len(albumResult) :
                    break;
                
            albumDict = {}
            albumDict['pid'] = albumResult[idx].pid
            albumDict['pic_path'] = albumResult[idx].pic_path
            albumDict['pic_desc'] = albumResult[idx].pic_desc
            albumDict['taoke_num_iid'] = albumResult[idx].taoke_num_iid
            albumDict['taoke_title'] = albumResult[idx].taoke_title
            albumDict['taoke_price'] = albumResult[idx].taoke_price
        
            currentPage['picArray'].append(albumDict)
        
        albumPagination['currentPage'] = currentPage
            
        resultDict['albumPagination'] = albumPagination
        
        '''
        相关推荐图集
        '''
        cursor = connection.cursor()
        cursor.execute('''SELECT count(*) as amount FROM (SELECT albunm_id FROM admin_picdetail 
                       WHERE categoary_id = %s group by albunm_id having count(*) > %s) a''',[cid,5])
        row = cursor.fetchone()
        
        offset = row[0]
        
        if offset > 8 :
            offset = random.randint(0,offset-8)
        
        
        cursor = connection.cursor()
        cursor.execute('''SELECT albunm_id ,albunm_name, count(*) as amount 
                        FROM admin_picdetail where categoary_id=%s group by albunm_id having count(*) > %s 
                        order by time desc limit %s offset %s ''',[cid,5,6,offset])
        #dao.getRecommendAlbumIdByMinAmount(5, 6, offset,int(cid));
        albumResults = cursor.fetchall()
        
        resultArray = []
        for row in albumResults:
            #albunm_id ,albunm_name, count(*) as amount
            albumDict = {}
            albumDict['albunmId'] = row[0]
            albumDict['albunmName'] = row[1]
            
            picResults = PicDetail.objects.filter(albunm_id=row[0])[:3] 
            
            picModelArray = []
    #            pid,pic_path,height,width,description,cate_id,root_cate_id,
    #                        albunm_name,albunm_id,user_id,time,taoke_num_iid,taoke_title,taoke_price'''
            for picRow in picResults:
                pDict = {}
                pDict['pid'] = picRow.pid
                pDict['pic_path'] = picRow.pic_path
                pDict['pic_desc'] = picRow.pic_desc
                
                picModelArray.append(pDict)
            
            albumDict['picDetail'] = picModelArray
            
            resultArray.append(albumDict)
            
        resultDict['recommendAlbum'] = resultArray
    
        jsonStr = json.dumps(resultDict,default=PicDetail.serialize)
    
        return HttpResponse(jsonStr,content_type="application/json") 
    
    except:
        pass
    
    return HttpResponse(jsonStr,content_type="application/json") 
    
    
def picdetail_album_pagination(request):
    ''' 图片详细信息中，图集分页接口 '''
    jsonStr='[]'
    
    try:
        '''
        图片详细信息中，图集分页接口
        [
            {
                "albunm_id": "22846230",
                "user_id": "176835576",
                "description": "纯棉面料，透气、宽松、舒适的上身感。一眼就看中了的活泼休闲范背心，多种粉嫩颜色的撞击，带来强烈的新鲜感，让简单的休闲背心，迸发激情，而且太好搭配了，随便穿穿都很有范儿！",
                "taoke_price": "38.00",
                "pid": "72059839",
                "root_cate_id": 0,
                "height": 245,
                "width": 220,
                "cate_id": 9,
                "time": "2013-04-21 17:02:44",
                "taoke_title": "女童2013新款百搭韩版休闲拼色格子夏装儿童宝宝童装吊带背心0720",
                "pic_path": "http://img01.taobaocdn.com/imgextra/i1/15576022115212799/T1av9jXwleXXXXXXXX_!!176835576-0-pix.jpg",
                "albunm_name": "花样背心造型拿满分",
                "taoke_num_iid": "17825693548"
            },
            ...
        ]
        '''
        pageSize = 6
        
        page = int(request.GET.get('p',None))
        albumId = request.GET.get('albumId',None)
        cid = request.GET.get('cid',None)
        
        if cid is None:
            HttpResponse('[]',content_type="application/json") 
        
        if albumId is None or len(albumId) < 3:
            albumId = None
        
        if page < 0:
            page = 0
        
        albumResults = PicDetail.objects.filter(categoary=Categoary(id=cid))
        
        if albumId is not None:
            albumResults = albumResults.filter(albunm_id=albumId)
    
        resultArray = list(albumResults[page*pageSize:(page+1)*pageSize])
        
        jsonStr = json.dumps(resultArray,default=PicDetail.serialize)
    
        return HttpResponse(jsonStr,content_type="application/json") 
        
    except:
        pass
    
    return HttpResponse(jsonStr,content_type="application/json") 

def runtime_param(request):
    
    appId = request.GET.get('appId',None)
    
    if appId is not None:
        app = App.objects.get(id=appId)
        
        runtime_param_dict = {}
        runtime_param_dict['taokeName']=app.taokeAccount.taokeName          #淘客账号名
        runtime_param_dict['appKey']=app.taobaoApiDetail.appKey             #api appKey
        runtime_param_dict['appSecret']=app.taobaoApiDetail.appSecret       #api appSecret
        
        jsonStr = json.dumps(runtime_param_dict)
    
        return HttpResponse(jsonStr,content_type="application/json") 
    
    return HttpResponse('[]',content_type="application/json") 


    