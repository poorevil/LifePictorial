'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class WlbTradeorderGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.sub_trade_id = None
		self.trade_id = None
		self.trade_type = None

	def getapiname(self):
		return 'taobao.wlb.tradeorder.get'
