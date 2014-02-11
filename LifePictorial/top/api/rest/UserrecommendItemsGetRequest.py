'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class UserrecommendItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.ext = None
		self.recommend_type = None

	def getapiname(self):
		return 'taobao.userrecommend.items.get'
