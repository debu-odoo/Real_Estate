{
    #  Information
    'name': 'Sale Order And Invoice',
    'description': 'Sale Order And Invoice',
    'version' :'15.0.1',
    'category': 'custome',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['sale'],
    'data': [
        'views/res_partner_views.xml' ,
        'reports/report.xml',
        'security/ir.model.access.csv',
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 