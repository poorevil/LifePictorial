'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class HanoiDatatemplateDetailDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.data_template_detail_ids = None
		self.data_template_vo = None

	def getapiname(self):
		return 'taobao.hanoi.datatemplate.detail.delete'
