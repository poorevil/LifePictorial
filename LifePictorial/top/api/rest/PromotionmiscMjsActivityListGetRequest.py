'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class PromotionmiscMjsActivityListGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_type = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.promotionmisc.mjs.activity.list.get'