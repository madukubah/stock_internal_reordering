# -*- coding: utf-8 -*-

{
    'name': 'POS Cash Back',
    'version': '1.0',
    'author': 'Technoindo.com',
    'category': 'Pont of Sales Management',
    'depends': [
        'account',
        'product',
        'sale',
        'point_of_sale',
    ],
    'data': [
        'views/menu.xml',
        'views/cashback.xml',
        'views/pos_cashback_templates.xml',
        'views/pos_config.xml',
        'views/pos_order.xml',
        'views/pos_session.xml',
        'views/pos_cashback_statement.xml',
    ],
    'qweb': [
        'static/src/xml/cashback_templates.xml',
    ],
    'demo': [
        # 'demo/sale_agent_demo.xml',
    ],
    'installable': True,
}
