'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class ProductGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.customer_props = None
		self.fields = None
		self.market_id = None
		self.product_id = None
		self.props = None

	def getapiname(self):
		return 'taobao.product.get'
