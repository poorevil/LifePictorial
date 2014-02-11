'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class SpContentDeletebyidsRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ids = None
		self.site_key = None

	def getapiname(self):
		return 'taobao.sp.content.deletebyids'
