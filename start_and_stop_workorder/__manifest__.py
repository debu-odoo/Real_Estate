{
    #  Information
    'name': 'Start And Stop Workorder',
    'description': 'Start And Stop Workorder',
    'version' :'15.0.1',
    'category': 'custom',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['mrp'],
    'data': [
        'views/mrp_workorder.xml',
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
}
