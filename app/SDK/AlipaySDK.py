#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import traceback
import config

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.domain.AlipayTradeAppPayModel import AlipayTradeAppPayModel
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayOfflineMaterialImageUploadRequest import AlipayOfflineMaterialImageUploadRequest
from alipay.aop.api.request.AlipayTradeAppPayRequest import AlipayTradeAppPayRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.response.AlipayOfflineMaterialImageUploadResponse import AlipayOfflineMaterialImageUploadResponse
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

alipayConfig = {
    "app_id": config.ConfigSite.Alipay_APPID,
    "app_private_key": config.ConfigSite.AliPay_AppPrivateKey,
    "alipay_public_key": config.ConfigSite.Alipay_PublicKey
}


alipay_client_config = AlipayClientConfig()
alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
alipay_client_config.app_id = alipayConfig["app_id"]
alipay_client_config.app_private_key = alipayConfig["app_private_key"]
alipay_client_config.alipay_public_key = alipayConfig["alipay_public_key"]


class AopClient():
    client = DefaultAlipayClient(
        alipay_client_config=alipay_client_config, logger=logger)
