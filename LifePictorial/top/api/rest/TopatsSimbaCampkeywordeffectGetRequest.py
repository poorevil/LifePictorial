'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class TopatsSimbaCampkeywordeffectGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.nick = None
		self.search_type = None
		self.source = None
		self.time_slot = None

	def getapiname(self):
		return 'taobao.topats.simba.campkeywordeffect.get'
