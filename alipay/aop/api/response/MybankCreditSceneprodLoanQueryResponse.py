#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodLoanQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodLoanQueryResponse, self).__init__()
        self._desc_msg = None
        self._info = None
        self._retry = None
        self._trace_id = None

    @property
    def desc_msg(self):
        return self._desc_msg

    @desc_msg.setter
    def desc_msg(self, value):
        self._desc_msg = value
    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodLoanQueryResponse, self).parse_response_content(response_content)
        if 'desc_msg' in response:
            self.desc_msg = response['desc_msg']
        if 'info' in response:
            self.info = response['info']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
