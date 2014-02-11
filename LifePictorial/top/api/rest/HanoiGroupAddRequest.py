'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class HanoiGroupAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.description = None
		self.group_code = None
		self.name = None
		self.open = None
		self.scene = None
		self.type = None

	def getapiname(self):
		return 'taobao.hanoi.group.add'
