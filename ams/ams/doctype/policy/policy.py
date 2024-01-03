# Copyright (c) 2023, JMG and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Policy(Document):


    def get_context(self, context):
        context.no_cache = 1
        context.show_sidebar = True
        context.title = self.title
        context.parents = [
            {"name": "admissions", "title": "All Student Admissions", "route": "admissions"}
            ]



def get_list_context(context=None):
	return {
		"title":"My Policies",
		"get_list": get_policy_list,
		"show_sidebar": True,
		"row_template": "templates/includes/policy_row.html",
		"no_breadcrumbs": False,
	}


def get_policy_list(doctype, txt, filters, limit_start, limit_page_length=20, order_by=None):
	from frappe.www.list import get_list

	user = frappe.session.user
	ignore_permissions = True

	if not filters:
		filters = []
	filters.append(("Policy", "owner", "=", user))

	return get_list(
		doctype, txt, filters, limit_start, limit_page_length, ignore_permissions=ignore_permissions
	)