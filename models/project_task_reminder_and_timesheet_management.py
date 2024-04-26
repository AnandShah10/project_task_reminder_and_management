from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta


class ProjectTaskNotifications(models.Model):
    _inherit = 'project.task'

    @api.model
    def send_email_reminder(self):
        print('00000000000000000000)')
        today = fields.Date.today()
        tomorrow = today + timedelta(days=1)
        print(today, tomorrow, 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')

        for i in self.env['project.task'].search([]):
            if i.date_deadline:
                print("task herekkkkkkkkkkkkkkkkkkkkkkkkkkkk", i.date_deadline.date(),
                      i.date_deadline.date() == today, i.date_deadline.date() == tomorrow)
                if i.date_deadline.date() == today or i.date_deadline.date() == tomorrow:
                    print("deadline is here1111111111111111111111")
                    for j in i.user_ids:
                        print("user got...............")
                        if j.login:
                            print('has a email.......................')
                            template = self.env.ref(
                                'project_task_reminder_and_management.project_task_deadline_reminder_mail_template')
                            print('tempalte done...........................')
                            email_values = {'email_to': 'mailto:' + j.login,
                                            'email_from': 'mailto:anandshah.odoo@gmail.com',
                                            'email_cc': False,
                                            'auto_delete': False,
                                            'message_type': 'user_notification',
                                            'recipient_ids': [j.id],
                                            'partner_ids': [],
                                            'scheduled_date': False,
                                            }
                            print("done setting email2222222222222222222222222")
                            template.send_mail(i.id, force_send=True, email_values=email_values)
                            print('done sending..........................')

    def send_daily_timesheet_entries(self):
        today = fields.Date.today()
        timesheet = self.env['account.analytic.line'].search([('date', '=', today)])
        print("time3333333333333333333333333", timesheet)
        project_timesheet = {}
        for i in timesheet:
            project_id = i.project_id.id
            if project_id not in project_timesheet:
                project_timesheet[project_id] = []
            project_timesheet[project_id].append(i)
            print(project_timesheet, 'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        for j, k in project_timesheet.items():
            project = self.env['project.project'].browse(j)
            print(project, 'pppppppppppppppppppppppppp')
            template = self.env.ref(
                'project_task_reminder_and_management.project_daily_timesheet_entries_mail_template')
            print('template..............................')
            email_values = {'email_to': 'mailto:' + project.user_id.login,
                            'email_from': 'mailto:anandshah.odoo@gmail.com',
                            'email_cc': False,
                            'auto_delete': False,
                            'message_type': 'user_notification',
                            'recipient_ids': [project.user_id.id],
                            'partner_ids': [],
                            'scheduled_date': False,
                            }
            print("done setting email2222222222222222222222222")
            template.send_mail(j, force_send=True, email_values=email_values)
            print('done sending..........................')
