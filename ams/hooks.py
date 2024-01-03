from . import __version__ as app_version

app_name = "ams"
app_title = "AMS"
app_publisher = "JMG"
app_description = "Agency Management System"
app_email = "grijalva10@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ams/css/ams.css"
# app_include_js = "/assets/ams/js/ams.js"

# include js, css files in header of web template
# web_include_css = "/assets/ams/css/ams.css"
# web_include_js = "/assets/ams/js/ams.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ams/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ams.utils.jinja_methods",
#	"filters": "ams.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ams.install.before_install"
# after_install = "ams.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ams.uninstall.before_uninstall"
# after_uninstall = "ams.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ams.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ams.tasks.all"
#	],
#	"daily": [
#		"ams.tasks.daily"
#	],
#	"hourly": [
#		"ams.tasks.hourly"
#	],
#	"weekly": [
#		"ams.tasks.weekly"
#	],
#	"monthly": [
#		"ams.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ams.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ams.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ams.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ams.utils.before_request"]
# after_request = ["ams.utils.after_request"]

# Job Events
# ----------
# before_job = ["ams.utils.before_job"]
# after_job = ["ams.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ams.auth.validate"
# ]

# website_route_rules = [
# 	{"from_route": "/orders", "to_route": "Sales Order"},
# 	{
# 		"from_route": "/orders/<path:name>",
# 		"to_route": "order",
# 		"defaults": {"doctype": "Sales Order", "parents": [{"label": "Orders", "route": "orders"}]},
# 	},
# 	{"from_route": "/invoices", "to_route": "Sales Invoice"},
# 	{
# 		"from_route": "/invoices/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Sales Invoice",
# 			"parents": [{"label": "Invoices", "route": "invoices"}],
# 		},
# 	},
# 	{"from_route": "/supplier-quotations", "to_route": "Supplier Quotation"},
# 	{
# 		"from_route": "/supplier-quotations/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Supplier Quotation",
# 			"parents": [{"label": "Supplier Quotation", "route": "supplier-quotations"}],
# 		},
# 	},
# 	{"from_route": "/purchase-orders", "to_route": "Purchase Order"},
# 	{
# 		"from_route": "/purchase-orders/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Purchase Order",
# 			"parents": [{"label": "Purchase Order", "route": "purchase-orders"}],
# 		},
# 	},
# 	{"from_route": "/purchase-invoices", "to_route": "Purchase Invoice"},
# 	{
# 		"from_route": "/purchase-invoices/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Purchase Invoice",
# 			"parents": [{"label": "Purchase Invoice", "route": "purchase-invoices"}],
# 		},
# 	},
# 	{"from_route": "/quotations", "to_route": "Quotation"},
# 	{
# 		"from_route": "/quotations/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Quotation",
# 			"parents": [{"label": "Quotations", "route": "quotations"}],
# 		},
# 	},
# 	{"from_route": "/shipments", "to_route": "Delivery Note"},
# 	{
# 		"from_route": "/shipments/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Delivery Note",
# 			"parents": [{"label": "Shipments", "route": "shipments"}],
# 		},
# 	},
# 	{"from_route": "/rfq", "to_route": "Request for Quotation"},
# 	{
# 		"from_route": "/rfq/<path:name>",
# 		"to_route": "rfq",
# 		"defaults": {
# 			"doctype": "Request for Quotation",
# 			"parents": [{"label": "Request for Quotation", "route": "rfq"}],
# 		},
# 	},
# 	{"from_route": "/addresses", "to_route": "Address"},
# 	{
# 		"from_route": "/addresses/<path:name>",
# 		"to_route": "addresses",
# 		"defaults": {"doctype": "Address", "parents": [{"label": "Addresses", "route": "addresses"}]},
# 	},
# 	{"from_route": "/boms", "to_route": "BOM"},
# 	{"from_route": "/timesheets", "to_route": "Timesheet"},
# 	{"from_route": "/material-requests", "to_route": "Material Request"},
# 	{
# 		"from_route": "/material-requests/<path:name>",
# 		"to_route": "material_request_info",
# 		"defaults": {
# 			"doctype": "Material Request",
# 			"parents": [{"label": "Material Request", "route": "material-requests"}],
# 		},
# 	},
# 	{"from_route": "/project", "to_route": "Project"},
# 	{"from_route": "/tasks", "to_route": "Task"},
# ]

website_route_rules = [
	{"from_route": "/policies", "to_route": "Policy"},
	{"from_route": "/quotes", "to_route": "Quote"},
	# {
	# 	"from_route": "/policies/<path:name>",
	# 	"to_route": "policies",
	# 	"defaults": {
	# 		"doctype": "Policy",
	# 		"parents": [{"label": "Policies", "route": "policies"}],
	# 	},
	# },
	# {"from_route": "/addresses", "to_route": "Address"},
	{
		"from_route": "/addresses/<path:name>",
		"to_route": "addresses",
		"defaults": {"doctype": "Address", "parents": [{"label": "Addresses", "route": "addresses"}]},
	}
]

standard_portal_menu_items = [
	{"title": "Policies", "route": "/policies", "reference_doctype": "Policy", "role": "Insured"},
	{"title": "Quotes", "route": "/quotes", "reference_doctype": "Quote", "role": "Insured"},
	{"title": "Invoices", "route": "/policies", "reference_doctype": "Policy", "role": "Insured"},
	{"title": "Tasks", "route": "/tasks", "reference_doctype": "ToDo", "role": "Insured"},

]

default_roles = [
	{"role": "Insured", "doctype": "Insured", "email_field": "email"}
]
