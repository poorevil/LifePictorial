'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class ItemSkuDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_num = None
		self.item_price = None
		self.lang = None
		self.num_iid = None
		self.properties = None

	def getapiname(self):
		return 'taobao.item.sku.delete'
