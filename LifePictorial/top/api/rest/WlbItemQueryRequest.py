'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class WlbItemQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_sku = None
		self.item_code = None
		self.item_type = None
		self.name = None
		self.page_no = None
		self.page_size = None
		self.parent_id = None
		self.status = None
		self.title = None

	def getapiname(self):
		return 'taobao.wlb.item.query'
