'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class SubuserDutyUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.duty_id = None
		self.duty_level = None
		self.duty_name = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.subuser.duty.update'
