# -*- coding: utf-8 -*-
{
    'name': "Service Team",

    'summary': """ Modul yang berfungsi sebagai """,

    'description': """
        Modul ini memiliki fitur :
        1. 
        2.
    """,

    'author': "Jakfar Siddiq",

    'website': "",

    'category': '',

    'version': '0.1',

    'depends': ['base', 'mail', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/service_team_views.xml',
        'views/booking_order_views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}
