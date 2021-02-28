# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
from datetime import datetime, timedelta


class HrpGaussDemandTestcase(models.Model):
    _name = 'hrp.gauss.demand.testcase'
    _description = 'Hrp Gauss Demand Testcase'

    # 需求编号
    requirement_number = fields.Char(string="需求编号", help="Requirement Number")
    # 特性名称
    name = fields.Char(string="特性名称", help="Property Name")
    # 开发人员
    # developers = fields.Char(string="开发人员", help="Developers")
    developers_id = fields.Many2one('hrp.gauss.demand.people.setting', string="开发人员", help="Developers",
                                    domain=[('type', '=', 'Developer')])
    # 测试owner
    test_owner_id = fields.Many2one('hrp.gauss.demand.people.setting', string="测试owner", help="Test Owner",
                                    domain=[('type', '=', 'Tester'), ('is_owner', '=', True)])
    # 测试参与人
    test_participants = fields.Many2many(comodel_name='hrp.gauss.demand.people.setting',
                                         relation='rel_demand_test_people', column1='test_people_id',
                                         column2='test_participants_id', string="测试参与人",
                                         help="Test Participants", domain=[('type', '=', 'Tester')])
    # 转测时间
    transfer_time = fields.Datetime(string="转测时间", help="Transfer time")
    # 文本用例数
    text_test_num = fields.Integer(string="文本用例数", help="Text testcase num")
    # 文本文件
    text_file = fields.Binary(string="文本文件", help="text file")
    # 自动化用例数
    auto_test_num = fields.Integer(string="自动化用例数", help="Auto testcase num")
    # 自动化率
    automation_rate = fields.Char(string="自动化率", help="Automation rate", compute='_compute_automation_rate', store=True)
    # 自动化用例路径
    auto_test_path = fields.Char(string="自动化用例路径", help="Auto testcase Path")
    # 测试完成时间
    completion_time = fields.Char(string="测试完成时间", help="Completion time",
                                  default=(fields.datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S%f'))
    # 备注
    note = fields.Text(string="备注", help="Note")
    # 状态
    state = fields.Boolean(string='是否测试完成', help='state')

    @api.depends('auto_test_num', 'text_test_num')
    def _compute_automation_rate(self):
        for rec in self:
            if rec.auto_test_num and rec.text_test_num:
                rec.automation_rate = '%.2f' % (rec.auto_test_num / rec.text_test_num * 100) + '%'
            else:
                rec.automation_rate = '0.00%'


class HrpGaussDfxTestcase(models.Model):
    _name = 'hrp.gauss.dfx.testcase'
    _description = 'Hrp Gauss Dfx Testcase'

    # DFX 能力
    name = fields.Char(string="DFX能力", help="Property Name")
    # 详细描述
    detailed_description = fields.Char(string="详细描述", help="Detailed description")

    # 所属模块
    test_mode = fields.Many2one('hrp.gauss.dfx.mode.setting', string="所属模块", help='Test mode')

    # 测试步骤
    test_procedure = fields.Text(string="测试步骤", help='Test mode')

    # 测试现象
    test_phenomenon = fields.Html(string="测试现象", help='Test phenomenon')

    # 测试发散
    test_divergence = fields.Text(string="测试发散", help='Test divergence')

    # 定位方式
    position_mode = fields.Many2many(comodel_name='hrp.gauss.dfx.position.setting',
                                     relation='rel_position_mode', column1='position_mode_id',
                                     column2='position_setting_id', string="定位方式", help='Position mode')

    # 测试用例路径
    testcase_path = fields.Char(string="用例路径", help='TestCase Path')

    # GAP
    gap = fields.Boolean(string="GAP", help="GAP")
    # 是否完成
    state = fields.Boolean(string="是否完成", help="State")

    line_ids = fields.One2many('hrp.gauss.dfx.testcase.line', 'head_id', string="笔记")


class HrpGaussDfxTestcaseLine(models.Model):
    _name = 'hrp.gauss.dfx.testcase.line'
    _description = 'Hrp Gauss Dfx Testcase Line'

    name = fields.Text(string="记录", help="Name")

    head_id = fields.Many2one('hrp.gauss.dfx.testcase', 'line_ids')

    recording_time = fields.Char(string="记录时间", help="Recording time",
                                 default=(fields.datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S%f'))


class HrpGaussFailureModeLibrary(models.Model):
    _name = 'hrp.gauss.failure.mode.library'
    _description = 'Hrp Gauss Failure Mode Library'

    # 二级故障对象
    secondary_fault_object = fields.Many2one('hrp.gauss.failure.mode.setting', string="二级故障对象",
                                             help='Secondary fault object', domain=[('level', '=', 'two')])

    # 三级故障对象
    three_fault_object = fields.Many2one('hrp.gauss.failure.mode.setting', string="三级故障对象",
                                         help='Three fault object', domain=[('level', '=', 'three')])

    # 组网方式
    networking_mode = fields.Many2one('hrp.gauss.networking.mode.setting', string="组网方式",
                                      help='Networking mode')

    # 故障模式描述
    name = fields.Char(string="故障模式描述", help="故障对象（故障表现）")

    # 故障场景构造方法
    fault_scenario_construction_method = fields.Text(string="故障场景构造方法", help="Fault scenario construction method")

    # 故障现象（运行）
    fault_phenomena_operation = fields.Text(string="故障现象（运行）", help="Fault phenomena (operation)")

    # 故障现象（重启）
    fault_phenomena_restart = fields.Text(string="故障现象（重启）", help="Fault phenomena (restart)")

    # 定位方式
    fault_position_mode = fields.Many2many(comodel_name='hrp.gauss.dfx.position.setting',
                                           relation='rel_fault_position_mode', column1='fault_position_mode_id',
                                           column2='position_setting_id', string="定位方式", help='Position mode')

    # 故障监控方法
    fault_monitoring_method = fields.Text(string="故障监控方法", help="Fault monitoring method")

    # 故障补偿措施
    fault_compensation_measures = fields.Text(string="故障补偿措施", help="Fault compensation measures")

    # 步骤记录（备注）
    note = fields.Html(string="步骤记录（备注）", help="Note")

    # 是否带有业务量
    is_data = fields.Boolean(string="是否带有业务量", help="data")

    # 业务量
    datas = fields.Char(string="业务量", help="datas")

    # 是否完成
    state = fields.Boolean(string="是否完成", help="State")

    # 测试完成时间
    completion_time = fields.Char(string="测试完成时间", help="Completion time",
                                  default=(fields.datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S%f'))
