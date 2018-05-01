# -*- coding: utf-8 -*-
# Copyright (c) 2018, Bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MaintenanceSchedule(Document):
	pass
	def on_submit(self):
		#update maintenance plan last date
		frappe.db.sql("""update `tabMaintenance Plan` set last_date="{}" where name="{}" and docstatus=1 """.format(self.date,self.plan),as_list=1)
		pass