'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class TmallEaiOrderRefundGoodReturnGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.refund_id = None
		self.refund_phase = None

	def getapiname(self):
		return 'tmall.eai.order.refund.good.return.get'
