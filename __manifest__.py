{
    'name': 'Client Moroso Management',
    'version': '1.1.0',
    'category': 'Sales',
    'author': 'Alphaqueb Consulting S.A.S.',
    'website': 'https://alphaqueb.com',
    'license': 'LGPL-3',
    'summary': 'Gestión manual de clientes morosos para Odoo 17 (con aplicación y menú propio)',
    'description': """
Módulo que permite:
- Marcar clientes como morosos y archivarlos.
- Desmarcarlos y reactivarlos.
- Visualizar una aplicación/menú específico con ícono para su gestión.
    """,
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/client_moroso_management_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/res_partner_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
