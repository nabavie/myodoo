{
    'name': 'Real Estate Apps',
    'version': '1.0',
    'category': 'Sales',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_view.xml',
        'views/menu_items.xml'
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
