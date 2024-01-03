frappe.views.calendar["Policy"] = {
	field_map: {
		start: "effective_date",
		end: "expiration_date",
		id: "name",
		title: "policy_number",
		allDay: "allDay",
		progress: "progress",
	},
	gantt: true,
// 	filters: [
// 		{
// 			fieldtype: "Link",
// 			fieldname: "reference_type",
// 			options: "Task",
// 			label: __("Task"),
// 		},
// 		{
// 			fieldtype: "Dynamic Link",
// 			fieldname: "reference_name",
// 			options: "reference_type",
// 			label: __("Task"),
// 		},
// 	],
	get_events_method: "frappe.desk.calendar.get_events",
};
