# -*- coding: utf-8 -*-

import time
from odoo import models, fields, api, tools, _
import logging
import requests
from hyper.contrib import HTTP20Adapter
import random

_logger = logging.getLogger(__name__)


class HrpGaussManagement(models.Model):
    _name = 'hrp.gauss.management'
    _description = 'Hrp Gauss Management'

    # 类别
    category_id = fields.Many2one('hrp.gauss.category', string='Category')
    # 测试所属模块
    owning_module = fields.Char(string="Owning Module")
    # 故障模式
    failure_mode = fields.Char(string='Failure mode')
    # 故障描述
    fault_description = fields.Char(string="Fault description")
    # 构造故障方法
    construction_failure_method = fields.Html(string="Construction failure method")
    # 故障现象（运行）
    trouble_phenomenon_operation = fields.Text(string='Trouble phenomenon (operation)')
    # 故障现象（重启）
    trouble_phenomenon_reboot = fields.Text(string='Trouble phenomenon (reboot)')
    # 故障报错来源
    source_fault_report = fields.Many2many('hrp.gauss.fault.report', string="Source of fault report")
    # 测试时间
    testing_time = fields.Datetime(string='Testing Time', default=fields.Datetime.now())
    # 测试人员
    # test_user = fields.Many2one('re')


class HrpGaussCategory(models.Model):
    _name = 'hrp.gauss.category'
    _description = 'Hrp Gauss Category'

    name = fields.Char('Category Name')

    category_ids = fields.One2many('hrp.gauss.management', 'category_id', string='Category')


class HrpGaussFaultReport(models.Model):
    _name = 'hrp.gauss.fault.report'
    _description = 'Hrp Gauss Fault Report'

    name = fields.Char('Source of fault name')


class HrpGaussSetting(models.Model):
    _name = 'hrp.gauss.setting'
    _description = 'Hrp Gauss Setting'

    name = fields.Char('Source of fault name')