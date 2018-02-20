# -*- coding: utf-8 -*-\
from lite.models import *
from lite.query.e_base import *
import datetime
import django.utils.timezone as timezone
class E_User(E_Base):
	def _PackDict(self,query_get):
		# print day
		_dict = {
			'is_vip':query_get.is_vip,
			'vip_deadline':query_get.vip_deadline.strftime("%Y-%m-%d"),
			'uuid':query_get.uuid,
			'show_pay':True,
			# 'day_num':_day_num,
		}
		return _dict

	# 1 点击标签 —— 获取供求
	def GetByID(self,user_id):
		_query = User.objects.get(id=user_id)
		return self._PackDict(_query)
	def GetBySession(self,session):
		_query = User.objects.get(session = session)
		return self._PackDict(_query)

	def UpdatePaySuccess(self,user_id):
		_user = User.objects.get(id = user_id)
		_user.is_vip = YES
		_user.vip_deadline = timezone.now() + timezone.timedelta(days=31)
		_user.save()