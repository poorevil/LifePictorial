'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class InventoryOccupyAdjustRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_unique_code = None
		self.items = None
		self.operate_time = None
		self.tb_order_type = None

	def getapiname(self):
		return 'taobao.inventory.occupy.adjust'
