'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class WangwangEserviceChatpeersGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.charset = None
		self.chat_id = None
		self.end_date = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.chatpeers.get'
