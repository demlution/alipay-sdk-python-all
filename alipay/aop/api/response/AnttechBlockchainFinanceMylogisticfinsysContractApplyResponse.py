#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceMylogisticfinsysContractApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceMylogisticfinsysContractApplyResponse, self).__init__()
        self._code = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceMylogisticfinsysContractApplyResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
