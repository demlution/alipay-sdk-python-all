#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CloudbusRoute import CloudbusRoute


class AlipayDataAiserviceCloudbusPredictbuslineSubmitModel(object):

    def __init__(self):
        self._app_version = None
        self._city_code = None
        self._partner_id = None
        self._route_version = None
        self._routes = None
        self._title = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def route_version(self):
        return self._route_version

    @route_version.setter
    def route_version(self, value):
        self._route_version = value
    @property
    def routes(self):
        return self._routes

    @routes.setter
    def routes(self, value):
        if isinstance(value, list):
            self._routes = list()
            for i in value:
                if isinstance(i, CloudbusRoute):
                    self._routes.append(i)
                else:
                    self._routes.append(CloudbusRoute.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.route_version:
            if hasattr(self.route_version, 'to_alipay_dict'):
                params['route_version'] = self.route_version.to_alipay_dict()
            else:
                params['route_version'] = self.route_version
        if self.routes:
            if isinstance(self.routes, list):
                for i in range(0, len(self.routes)):
                    element = self.routes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.routes[i] = element.to_alipay_dict()
            if hasattr(self.routes, 'to_alipay_dict'):
                params['routes'] = self.routes.to_alipay_dict()
            else:
                params['routes'] = self.routes
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceCloudbusPredictbuslineSubmitModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'route_version' in d:
            o.route_version = d['route_version']
        if 'routes' in d:
            o.routes = d['routes']
        if 'title' in d:
            o.title = d['title']
        return o


