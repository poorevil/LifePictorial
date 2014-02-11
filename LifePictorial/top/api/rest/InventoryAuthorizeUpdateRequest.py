'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class InventoryAuthorizeUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.authorize_code = None
		self.quantity = None
		self.sc_item_id = None

	def getapiname(self):
		return 'taobao.inventory.authorize.update'
