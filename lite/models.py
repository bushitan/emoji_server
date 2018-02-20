#coding:utf-8
from django.db import models

# Create your models here.
import django.utils.timezone as timezone
import datetime
from lite.lib.util import *
from lite.lib.image_save import *
class User(models.Model):
	name =  models.CharField(max_length=100, verbose_name=u'姓名',default="",null=True,blank=True)
	is_vip = models.IntegerField(u'是否老板',default=NO,choices=IS_VIP.items(),null=True,blank=True)
	uuid =  models.CharField(max_length=32, verbose_name=u'会员编号',null=True,blank=True)
	wx_union_id = models.CharField(max_length=50, verbose_name=u'微信UnionID',null=True,blank=True)
	wx_open_id = models.CharField(max_length=50, verbose_name=u'微信OpenID',null=True,blank=True)
	wx_session_key = models.CharField( max_length=128,verbose_name=u'微信SessionKey',null=True,blank=True)
	wx_expires_in = models.FloatField( verbose_name=u'微信SessionKey过期时间',null=True,blank=True)
	session = models.CharField (max_length=128, verbose_name=u'Django的session',null=True,blank=True)
	expires = models.FloatField( verbose_name=u'Django的session过期时间',null=True,blank=True)

	vip_deadline = models.DateTimeField(u'VIP到期时间', default = timezone.now)
	create_time = models.DateTimeField(u'创建时间', default = timezone.now)

	class Meta:
		verbose_name_plural = verbose_name = u'1 用户'
		# app_label = string_with_title(u'api', u"23421接口")

	def __unicode__(self):
		return '%s' % (self.id)

class Order(models.Model):
	user = models.ForeignKey(User, verbose_name=u'用户名称')
	wx_out_trade_no = models.CharField(max_length=32, verbose_name=u'微信_商户订单号',null=True,blank=True)
	is_pay =  models.IntegerField(u'支付状态',default=NO,choices=IS_PAY.items())
	pay_price = models.FloatField( verbose_name=u'支付价格',null=True,blank=True)
	pay_time = models.DateTimeField(u'支付时间', default = timezone.now)
	create_time = models.DateTimeField(u'创建时间',default = timezone.now)
	class Meta:
		verbose_name_plural = verbose_name = u'2 支付订单'
	def __unicode__(self):
		return '%s' % (self.id)

class Image(models.Model):
	url = models.CharField(max_length=500, verbose_name=u'地址',default="",null=True,blank=True)
	local_path = models.ImageField(u'图标',upload_to='img/',null=True,blank=True)
	create_time = models.DateTimeField(u'创建时间',default = timezone.now)
	class Meta:
		verbose_name_plural = verbose_name = u'3 图片'
		ordering = ['-create_time']
	def __unicode__(self):
		return '%s' % (self.id)
	def save(self):
		ImageSave(self,Image)