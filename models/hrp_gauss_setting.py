# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _


class HrpGaussDemandPeopleSetting(models.Model):
    _name = 'hrp.gauss.demand.people.setting'
    _description = 'Hrp Gauss Demand People Setting'

    # name
    name = fields.Char(string="姓名", help='Name')

    type = fields.Selection(string='类别', selection=[('Tester', '测试'), ('Developer', '开发')])
    is_owner = fields.Boolean(string="是否测试Owner", default=False)


class HrpGaussDfxModeSetting(models.Model):
    _name = 'hrp.gauss.dfx.mode.setting'
    _description = 'Hrp Gauss Dfx Mode Setting'

    # name
    name = fields.Char(string="模块名", help='Name')


class HrpGaussDfxPositionSetting(models.Model):
    _name = 'hrp.gauss.dfx.position.setting'
    _description = 'Hrp Gauss Dfx Position Setting'

    # name
    name = fields.Char(string="方式名", help='Name')


class HrpGaussFailureModeSetting(models.Model):
    _name = 'hrp.gauss.failure.mode.setting'
    _description = 'Hrp Gauss Failure Mode Setting'

    # name
    name = fields.Char(string="故障名称", help='Name')

    level = fields.Selection(string='级别', selection=[('two', '二'), ('three', '三')])


class HrpGaussNetworkingModeSetting(models.Model):
    _name = 'hrp.gauss.networking.mode.setting'
    _description = 'Hrp Gauss Networking Mode Setting'

    # name
    name = fields.Char(string="组网方式", help='Name')
