{
    #  Information
    'name': 'Contact And Product Unique Code ',
    'description': 'Contact And Product Unique Code',
    'version' :'15.0.1',
    'category': 'Sales',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': '',

    # Dependency
    'depends': ['stock'],
    'data': [
      
      'views/product_category.xml',
      'data/product_sequence.xml',
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,
} 