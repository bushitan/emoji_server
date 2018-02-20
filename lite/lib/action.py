# -*- coding: utf-8 -*-

from lite.lib.util import *
from lite.query.e_image import *
from lite.query.e_user import *
from lite.query.e_order import *
from lite.lib.wx_api import *
import datetime,random,xml
from django.db import transaction #事务
e_user = E_User()
e_image = E_Image()
e_order = E_Order()
class Action():
    def UserGetBySession(self,session):
        return e_user.GetBySession(session)

    def PayCreate(self,user):
        wx_out_trade_no = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + str(user.id) + str(int(random.random() * 1000))

        _pay_price = '95'  # 0.95元
        if e_order.CheckByUserID(user.id) is True:
            e_order.UpdateByTradeNo(user.id , wx_out_trade_no,_pay_price)
        else:
            e_order.Create(user.id , wx_out_trade_no,_pay_price)

        _wx_pay = wx_pay( user.wx_open_id , wx_out_trade_no ,_pay_price)
        wx_dict  =  _wx_pay.get_request_payment()
        return wx_dict

    def PayCallBack(self,_xml):
        xh = XMLHandler()
        xml.sax.parseString( _xml, xh)
        _xml_dict = xh.getDict()
        _out_trade_no = _xml_dict["out_trade_no"]
        _total_fee = _xml_dict["total_fee"]
        #返回结果
        _xml_resualt = '''
        <xml>
          <return_code><![CDATA[%s]]></return_code>
          <return_msg><![CDATA[%s]]></return_msg>
        </xml>
        '''
        try:
            with transaction.atomic():
                print 1
                print _out_trade_no
                _user_id = e_order.UpdatePaySuccessByTradeNo(_out_trade_no)
                print 11
                print _user_id
                e_user.UpdatePaySuccess(_user_id)
                print 12
                return _xml_resualt%("SUCCESS",u"支付成功")
        except Exception ,e:
            return _xml_resualt%("FAIL",u"支付失败，请重试")


    def ImageGetList(self):
        return e_image.GetList()
        #订单存在未支付，覆盖 else 创建新订单
        # if Order.objects.filter(user_id = user_id,is_payment = IS_PAYMENT_FALSE).exists() is True:
        #     _order = Order.objects.get(user_id = user_id,is_payment = IS_PAYMENT_FALSE)
        # else:
        #     _order = Order(user_id = user_id )
        # _order.wx_out_trade_no = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + str(_order.id) + str(int(random.random() * 1000))
        # _order.start_time = datetime.datetime.now()
        # _during =  DAY_MEMBER if is_member is True else  DAY_SINGLE #点播3天，会员1年
        # _order.end_time = datetime.datetime.now() + datetime.timedelta(days = _during)
        # _order.create_time = datetime.datetime.now()
        # return _order
