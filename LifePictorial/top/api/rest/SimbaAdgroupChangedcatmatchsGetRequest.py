'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class SimbaAdgroupChangedcatmatchsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.simba.adgroup.changedcatmatchs.get'
