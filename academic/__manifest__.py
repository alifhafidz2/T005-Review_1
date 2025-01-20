{
    'name': 'Academic Information System v1.0',
    'version': '1.0',
    'author': 'Alif Hafidz',
    'depends': ['base'],
    'category': 'Education',
    'website': 'https://github.com/alifhafidz/academic-information-system',
    'description': """
    Academic Information System is a web application that allows users to manage their academic information such as courses, exams, and grades. It also provides a dashboard for users to view their grades and progress.'
    """,
    'data': [
        'security/ir.model.access.csv',
        'menu.xml',
        'course.xml',
        'session.xml',
        'attendee.xml',
        'partner.xml',
        'wizard/create_attendee.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}