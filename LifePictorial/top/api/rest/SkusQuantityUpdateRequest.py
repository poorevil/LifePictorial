'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class SkusQuantityUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.num_iid = None
		self.outerid_quantities = None
		self.skuid_quantities = None
		self.type = None

	def getapiname(self):
		return 'taobao.skus.quantity.update'
