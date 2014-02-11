'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class WlbOrderScheduleRuleAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.backup_store_id = None
		self.default_store_id = None
		self.option = None
		self.prov_area_ids = None

	def getapiname(self):
		return 'taobao.wlb.order.schedule.rule.add'
