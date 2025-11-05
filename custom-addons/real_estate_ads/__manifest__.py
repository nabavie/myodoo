{
    "name": "Real Estate Apps",
    "version": "1.0",
    "website": "https://faradia.org",
    "author": "Alireza Nabavieh",
    "description": """
        Real Estate Module to manage and display property listings (This is Test!!!)
    """,
    "category": "Sales",
    "depends": ['base'],
    "data": [
        'security/ir.model.access.csv',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_view.xml',
        'views/menu_items.xml'
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3"
}