# -*- coding: utf-8 -*-
{
    'name': '客户',
    'version': '12.0.1.0',
    'summary': '客户',
    'author': "www.mypscloud.com",
    'website': 'https://www.mypscloud.com/',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        #'security/ir.model.access.csv',
        #'wizard/student_regiester_views.xml',
        #'views/res_partner_views.xml',
        #'views/training_lesson_views.xml',
        #'views/training_subject_views.xml',
        #'views/training_views.xml',
        'views/pscloud_subject_views.xml',
        'views/pscloud_views.xml',
    ],
    'qweb': [],
    'js': [],
    'css': [],
    'auto_install': False,
    'application': True,
}
