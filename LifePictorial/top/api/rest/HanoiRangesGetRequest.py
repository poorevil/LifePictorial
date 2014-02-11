'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class HanoiRangesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.current_page = None
		self.document_id = None
		self.id = None
		self.key = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.hanoi.ranges.get'
