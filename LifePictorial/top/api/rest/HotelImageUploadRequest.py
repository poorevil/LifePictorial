'''
Created by auto_sdk on 2014-02-10 16:59:30
'''
from top.api.base import RestApi
class HotelImageUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.hid = None
		self.pic = None

	def getapiname(self):
		return 'taobao.hotel.image.upload'

	def getMultipartParas(self):
		return ['pic']
