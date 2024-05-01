# -*- coding: utf-8 -*-
{
    'name': "Mantenimiento Preventivo",

    'summary': """
        Listado de los futuros mantenimientos preventivos a realizar a los clientes,
        así como su seguimiento y paso a facturación""",

    'description': """
        Control del mantenimiento preventivo que se realiza a los clientes
    """,

    'author': "Isabel Marti Romeu",
    'website': "https://isabelmartiromeu.github.io/mantenprev/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/orden_facturacion_report.xml',
        'reports/informe_report.xml',
        'reports/certificado_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
