#coding:utf-8

import json

from django.http import HttpResponse
from django.views.generic import ListView

from lib.message import *
from models import *
import datetime
import  emoji_server.settings  as SETTINGS
from lite.lib.util import *
from lite.lib.weixin import *
from lite.lib.action import *
action = Action()
#1 首页文章初始化
# class Index( ListView):
#     def get(self, request, *args, **kwargs):
#         try:
#             print 11111
#             _dict = {
#                 'MSG':u'登录初始化成狗',
#             }
#             print _dict
#             return MESSAGE_RESPONSE_SUCCESS(_dict)
#         except Exception,e :
#             return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#1

# 3 获取生词库
class Login( ListView):
	def get(self, request, *args, **kwargs):
		# try:
			_js_code = request.GET.get('js_code',"")
			_session = request.GET.get('session',"")
			_wx = WeiXin()
			_check_session = _wx.UserLoginCheckSession(_js_code,_session)
			_user_dict = action.UserGetBySession(_check_session)
			# _check_session = _wx._GetOpenID(_js_code)
			_dict = {
				"session":_check_session ,
				"user_dict":_user_dict ,
			}
			print _dict
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		# except Exception,e :
		# 	return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



# 微信支付
class WXCreate( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_session = request.GET.get('session',"")
			print _session
			_user = User.objects.get(session = _session)
			wx_dict = action.PayCreate(_user)
			_dict = {
				"wx_dict":wx_dict,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


# 微信支付
class WXCallback( ListView):
	def post(self, request, *args, **kwargs):
		try:
			_xml_request =  request.body
			wx_dict = action.PayCallBack(_xml_request)
			_dict = {
				"wx_dict":wx_dict,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
# 微信支付
class ImageGetList( ListView):
	def get(self, request, *args, **kwargs):
		try:
			_cover_list = action.ImageGetList()
			_dict = {
				"cover_list":_cover_list,
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

import base64
# 微信支付
class UploadGetToken( ListView):
	def get(self, request, *args, **kwargs):
		try:

			_user = User.objects.get(session = request.GET.get('session',""))
			# _style = request.GET.get('style',"")
			# _suffix = request.GET.get('suffix',"")  #后缀
			_suffix = "jpg"
			#按照当前时间和用户生成名字
			_file_name = "emoji_" + str(_user.id) + "_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "." + _suffix

			_qn = QiNiu()
			token,key =_qn.getBase64Token(_file_name)
			_dict = {
				"token":token,
				"key": base64.b64encode(key),
			}
			return MESSAGE_RESPONSE_SUCCESS(_dict)
		except Exception,e :
			return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

