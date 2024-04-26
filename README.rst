=============================================
Module Documentation: Task Reminder & Timesheet
=============================================

Overview
--------

The Task Reminder & Timesheet module provides functionality within Odoo to automate reminders for tasks nearing their deadline and to send daily timesheet entries of projects to the project manager by email.

Features
--------

1. **Task Reminders**:
   - Automatically sends reminders to responsible users one day before the task deadline.
   - Sends reminders if the task deadline is today.

2. **Daily Timesheet Entries**:
   - Automatically compiles and sends daily timesheet entries of projects to the project manager via email.

Installation
------------

1. Clone this repository to your local machine:

    ```
    git clone <repository-url>
    ```

2. Install the module in your Odoo instance.

3. Restart Odoo to apply the changes.

Usage
-----

1. Task Reminders:
   - Configure task deadlines and responsible users within Odoo tasks.
   - Ensure that the cron job is set up to run daily to send reminders.

2. Daily Timesheet Entries:
   - Set up projects and associate employees with tasks.
   - The module automatically compiles daily timesheet entries and sends them to the project manager's email.

Contributing
------------

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

License
-------

This module is licensed under the MIT License. See the LICENSE file for details.

Credits
-------

This module was developed by Anand Shah. For any inquiries, please contact shahanand1072004@gmail.com.

