'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class PromotionCouponsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.coupon_id = None
		self.denominations = None
		self.end_time = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.promotion.coupons.get'