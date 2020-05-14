#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncApbillBillcustviewBatchqueryModel(object):

    def __init__(self):
        self._bill_nos = None

    @property
    def bill_nos(self):
        return self._bill_nos

    @bill_nos.setter
    def bill_nos(self, value):
        if isinstance(value, list):
            self._bill_nos = list()
            for i in value:
                self._bill_nos.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_nos:
            if isinstance(self.bill_nos, list):
                for i in range(0, len(self.bill_nos)):
                    element = self.bill_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_nos[i] = element.to_alipay_dict()
            if hasattr(self.bill_nos, 'to_alipay_dict'):
                params['bill_nos'] = self.bill_nos.to_alipay_dict()
            else:
                params['bill_nos'] = self.bill_nos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncApbillBillcustviewBatchqueryModel()
        if 'bill_nos' in d:
            o.bill_nos = d['bill_nos']
        return o


