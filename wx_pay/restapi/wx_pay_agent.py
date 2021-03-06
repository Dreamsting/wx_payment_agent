#!usr/bin/env python
# -*- coding: utf8 -*-
#
# 微信支付代理--基于Flask的RESTful Web服务
#
# Created on 2016-04-12
# author: shaojianyong
#
################################################################################

import logging
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from wx_pay.payment.wx_unified_order import WxUnifiedOrder
from wx_pay.payment.wx_order_query import WxOrderQuery
from wx_pay.refund.wx_refund_query import WxRefundQuery
from wx_pay.refund.wx_refund_apply import WxRefundApply
from wx_pay.reconcile.wx_bill_download import WxBillDownload

app = Flask(__name__)
api = Api(app)

# 微信统一下单
class WxUnifiedOrderRes(Resource):
    # 微信下单
    def post(self):
        params = request.get_json(force=True)
        
        handler = WxUnifiedOrder()
        return jsonify(handler.unified_order(params))

# 微信订单查询
class WxOrderQueryRes(Resource):
    # 查询微信订单
    def get(self, order_id):
        handler = WxOrderQuery()
        return jsonify(handler.query_order_info(order_id))

# 微信退款申请
class WxRefundApplyRes(Resource):
    # 发起退款请求
    def post(self):
        params = request.get_json(force=True)
        
        handler = WxRefundApply()
        return jsonify(handler.apply_for_refund(params))

# 微信退款查询
class WxRefundQueryRes(Resource):
    # 查询退款记录
    def get(self, order_id):
        handler = WxRefundQuery()
        return jsonify(handler.query_refund_records(order_id))

# 微信对账单下载
class WxBillDownloadRes(Resource):
    # 获取微信对账单
    def get(self, bill_date):
        handler = WxBillDownload()
        return jsonify(handler.download_bill(bill_date))

# RESTful API
api.add_resource(WxUnifiedOrderRes, '/wx-pay/unified-order')
api.add_resource(WxOrderQueryRes, '/wx-pay/order-query/<order_id>')

api.add_resource(WxRefundApplyRes, '/wx-pay/refund-apply')
api.add_resource(WxRefundQueryRes, '/wx-pay/refund-query/<order_id>')

api.add_resource(WxBillDownloadRes, '/wx-pay/bill-download/<bill_date>')

# 单元测试
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='wx_refund_agent.log',
                        filemode='a')
    logging.getLogger().addHandler(logging.StreamHandler())
    
    app.run(debug=True)
