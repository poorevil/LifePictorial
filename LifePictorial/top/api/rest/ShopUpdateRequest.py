'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class ShopUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.bulletin = None
		self.desc = None
		self.title = None

	def getapiname(self):
		return 'taobao.shop.update'
