'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class PromotionCouponAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.condition = None
		self.denominations = None
		self.end_time = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.promotion.coupon.add'
