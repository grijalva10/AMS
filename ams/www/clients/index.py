import frappe


def get_context(context):
    current_user = frappe.session.user
    insured_list = frappe.get_list('Insured', filters={'agent': current_user}, fields=['*'])
    return insured_list