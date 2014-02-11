'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class CrmGrademktMemberGradeactivityInitRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.feather = None
		self.parameter = None

	def getapiname(self):
		return 'taobao.crm.grademkt.member.gradeactivity.init'
