# -*- coding: utf-8 -*-
{
    'name': "GAUSSDB TEST",

    'summary': 'GAUSS数据',

    'description': """此模块进行GAUSS 测试数据的整理，汇总。主要是高可用的DFX等信息汇总。""",

    'author': "li kaifeng",
    'website': "https:/www.huawei.com",
    'category': 'li kaifeng',
    'version': '14.0.1',
    'installable': True,
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        'data/gauss_data.xml',
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/menuitem_gauss.xml',
        # 'views/hrp_gauss_management_view.xml',
        'views/hrp_gauss_setting_view.xml',
        'views/hrp_gauss_demand_testcase_view.xml',
        'views/hrp_gauss_dfx_testcase_view.xml',
    ],
    'application': True,
}
