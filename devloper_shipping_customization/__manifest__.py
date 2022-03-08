{
    #  Information
    'name': 'Devloper Shipping Customization',
    'description': 'devloper shipping customization',
    'version' :'15.0.1',
    'category': 'Sales',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['contacts' , 'sale_management' , 'sale_stock' , 'stock'],
    'data': [
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 