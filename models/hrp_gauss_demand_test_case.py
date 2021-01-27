# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _


class HrpGaussDemandTestcase(models.Model):
    _name = 'hrp.gauss.demand.testcase'
    _description = 'Hrp Gauss Demand Testcase'

    # 需求编号
    requirement_number = fields.Char("Requirement Number")
    # 特性名称
    property_name = fields.Char("Property Name")
    # 开发人员
    developers = fields.Char("Developers")
    # 测试owner
    test_owner = fields.Char("Test Owner")
    # 测试参与人
    test_participants = fields.Char("Test Participants")
    # 转测时间
    transfer_time = fields.Datetime("Transfer time")
    # 文本用例数
    text_test_num = fields.Integer("Text testcase num")
    # 文本文件
    text_file = fields.Binary("text file")
    # 自动化用例数
    auto_test_num = fields.Integer("Auto testcase num")
    # 自动化率
    automation_rate = fields.Char("Automation rate", compute='_compute_automation_rate')
    # 自动化用例路径
    auto_test_path = fields.Char("Auto testcase Path")
    # 测试完成时间
    completion_time = fields.Char("Completion time", default=fields.Datetime.now())
    # 备注
    note = fields.Text("Note")
    # 状态
    state = fields.Boolean('state')

    @api.depends('auto_test_num', 'text_test_num')
    def _compute_automation_rate(self):
        for rec in self:
            if rec.auto_test_num and rec.text_test_num:
                rec.automation_rate = '%.2f' % (rec.auto_test_num / rec.text_test_num*100)+'%'
            else:
                rec.automation_rate = '0.00%'
