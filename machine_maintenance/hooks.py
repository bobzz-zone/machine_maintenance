# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "machine_maintenance"
app_title = "Machine Maintenance"
app_publisher = "Bobby"
app_description = "Apps For Machine Maintenance"
app_icon = "octicon octicon-history"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/machine_maintenance/css/machine_maintenance.css"
# app_include_js = "/assets/machine_maintenance/js/machine_maintenance.js"

# include js, css files in header of web template
# web_include_css = "/assets/machine_maintenance/css/machine_maintenance.css"
# web_include_js = "/assets/machine_maintenance/js/machine_maintenance.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "machine_maintenance.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "machine_maintenance.install.before_install"
# after_install = "machine_maintenance.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "machine_maintenance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
# 	"all": [
# 		"machine_maintenance.tasks.all"
# 	],
	"daily": [
		"machine_maintenance.task.daily"
	],
# 	"hourly": [
# 		"machine_maintenance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"machine_maintenance.tasks.weekly"
# 	]
# 	"monthly": [
# 		"machine_maintenance.tasks.monthly"
# 	]
}

# Testing
# -------

# before_tests = "machine_maintenance.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "machine_maintenance.event.get_events"
# }

