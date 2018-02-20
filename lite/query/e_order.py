# -*- coding: utf-8 -*-
from lite.models import *
from lite.query.e_base import *
from lite.lib.util import *

class E_Order(E_Base):
	def _PackDict(self,query_get):
		_dict = {
			'user_id':query_get.user_id,
			'order_id':query_get.id,
			'wx_out_trade_no':query_get.wx_out_trade_no,
			'is_pay':query_get.is_pay,
			'pay_price':query_get.pay_price,
			'pay_time':query_get.pay_time,
		}
		return _dict

	def GetByUserID(self,user_id):
		_order = Order.objects.filter(user_id=user_id)
		return self._PackDict(_order)
	# 1 点击标签 —— 获取供求
	def CheckByUserID(self,user_id):
		return Order.objects.filter(user_id=user_id).exists()

	def UpdateByTradeNo(self,user_id,wx_out_trade_no,pay_price):
		_order = Order.objects.get(user_id=user_id)
		_order.wx_out_trade_no = wx_out_trade_no
		_order.pay_price = pay_price
		_order.save()
	def Create(self,user_id,wx_out_trade_no,pay_price):
		_order = Order(
			user_id = int(user_id),
			wx_out_trade_no = wx_out_trade_no,
			pay_price = pay_price,
		)
		_order.save()


	def GetBySession(self,session):
		_query = User.objects.get(session = session)
		return self._PackDict(_query)

	def UpdatePaySuccessByTradeNo(self,_out_trade_no):
		_order = Order.objects.get(wx_out_trade_no = _out_trade_no)
		_order.is_pay = YES
		_order.save()
		return _order.user_id