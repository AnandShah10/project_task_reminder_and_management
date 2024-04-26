# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'project_task_reminder_and_management',
    'version': '1.5',
    'summary': "Project management module",
    'sequence': 13,
    'author': "anand",
    'description': """
Project Management module to amnage task deadlines and timesheets 
""",
    'category': 'Custom/Project',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['project','base'],
    'data': [
        'data/cronjob.xml',
        'data/deadline_reminder_mail_template.xml',
        'data/daily_time_sheet_entry_mail.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'module_type': 'official',
}
