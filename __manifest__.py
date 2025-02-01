{
    'name': 'Client Moroso Management',
    'version': '1.2.0',
    'category': 'Sales',
    'author': 'Alphaqueb Consulting S.A.S.',
    'website': 'https://alphaqueb.com',
    'license': 'LGPL-3',
    'summary': 'Gestión manual de clientes morosos para Odoo 17 (con aplicación y menú propio)',
    'description': """
        ...
    """,
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/client_moroso_management_security.xml',
        'security/ir.model.access.csv',
        # IMPORTANTE: Cargar primero res_partner_view.xml
        'views/res_partner_view.xml',
        # Luego el menú que referencia la vista
        'views/menu.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
