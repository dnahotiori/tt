#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserAnalysisData import UserAnalysisData


class AlipayOpenPublicUserDataBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicUserDataBatchqueryResponse, self).__init__()
        self._data_list = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, UserAnalysisData):
                    self._data_list.append(i)
                else:
                    self._data_list.append(UserAnalysisData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicUserDataBatchqueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
