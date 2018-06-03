from __future__ import unicode_literals
import frappe
from frappe.utils import now , nowdate ,add_days
def daily():
	list_sc = frappe.db.sql("""select name ,last_date ,email, machine , maintenance_sop ,type , maintenance_frequency , lead_time,reschedule , frequency,work_type,level,technician, duration,sop
		from `tabMaintenance Plan`
		where docstatus=1 and stop=0 and datediff("{}",last_date )=frequency-lead_time
	 """.format(now()),as_dict=1)
	for row in list_sc:
		sparepart_list = frappe.db.sql("""select sparepart,qty from `tabSparepart Table` where parent="{}" """.format(row["name"]),as_dict=1)
		sparepart=[]
		for det in sparepart_list:
			sparepart.append({"doctype":"Schedule Sparepart Table","sparepart":det["sparepart"],"qty":det["qty"]})
		doc = frappe.get_doc({
			"doctype": "Maintenance Schedule",
			"machine":row["machine"],
			"plan":row["name"],
			"maintenance_sop":row["maintenance_sop"],
			"type":row["type"],
			"date":add_days(now(),row("lead_time")),
			"lead_time":row["lead_time"],
			"reschedule":row["reschedule"],
			"work_type":row["work_type"],
			"level":row["level"],
			"technician":row["technician"],
			"duration":row["duration"],
			"sop":row["sop"],
			"prev_date":row["last_date"],
			"email":row["email"],
			"items":sparepart
			})
		doc.insert()

def test():
	list_sc = frappe.db.sql("""select name ,last_date ,email, machine , maintenance_sop ,type , maintenance_frequency , lead_time,reschedule , frequency,work_type,level,technician, duration,sop
		from `tabMaintenance Plan`
		where docstatus=1 and stop=0
	 """.format(now()),as_dict=1)
	for row in list_sc:
		sparepart_list = frappe.db.sql("""select sparepart,qty from `tabSparepart Table` where parent="{}" """.format(row["name"]),as_dict=1)
		sparepart=[]
		for det in sparepart_list:
			sparepart.append({"doctype":"Schedule Sparepart Table","sparepart":det["sparepart"],"qty":det["qty"]})
		doc = frappe.get_doc({
			"doctype": "Maintenance Schedule",
			"machine":row["machine"],
			"plan":row["name"],
			"maintenance_sop":row["maintenance_sop"],
			"type":row["type"],
			"date":add_days(now(),row("lead_time")),
			"lead_time":row["lead_time"],
			"reschedule":row["reschedule"],
			"work_type":row["work_type"],
			"level":row["level"],
			"technician":row["technician"],
			"duration":row["duration"],
			"sop":row["sop"],
			"prev_date":row["last_date"],
			"email":row["email"],
			"items":sparepart
			})
		doc.insert()
	