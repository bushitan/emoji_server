# -*- coding: utf-8 -*-
from lite.models import *
from lite.query.e_base import *

class E_Image(E_Base):
	def _PackDict(self,query_get):
		_dict = {
			'image_url':query_get.url,
			'image_url':query_get.url,
		}
		return _dict

	# 1 点击标签 —— 获取供求
	def GetList(self):
		_query = Image.objects.all()
		return self._PackList(self._PackDict,_query)