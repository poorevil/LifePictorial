'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.order_ids = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.get'
