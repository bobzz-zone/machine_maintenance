# -*- coding: utf-8 -*-
# Copyright (c) 2018, Bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MaintenancePlan(Document):
	pass
	def on_submit(self):
		self.last_date=self.start_date