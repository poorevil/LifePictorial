'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class UmpRangeDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.act_id = None
		self.ids = None
		self.type = None

	def getapiname(self):
		return 'taobao.ump.range.delete'
