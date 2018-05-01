// Copyright (c) 2018, Bobby and contributors
// For license information, please see license.txt

frappe.ui.form.on('Maintenance Schedule', {
	refresh: function(frm) {
// cur_frm.add_fetch(link_field, source_fieldname, target_fieldname);
cur_frm.add_fetch("maintenance_sop", "type", "type");
cur_frm.add_fetch("maintenance_sop", "work_type", "work_type");
cur_frm.add_fetch("maintenance_sop", "level", "level");
cur_frm.add_fetch("maintenance_sop", "duration", "duration");
cur_frm.add_fetch("maintenance_sop", "sop", "sop");
cur_frm.add_fetch("technician", "email", "email");
	}
});
