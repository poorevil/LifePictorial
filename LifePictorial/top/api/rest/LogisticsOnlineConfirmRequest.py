'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class LogisticsOnlineConfirmRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_split = None
		self.out_sid = None
		self.seller_ip = None
		self.sub_tid = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.online.confirm'
