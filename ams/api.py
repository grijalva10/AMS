from datetime import datetime
import frappe


@frappe.whitelist()
def create_close_lead(lead_id=None, contact_id=None, lead_name=None,
                      annual_payroll=None, annual_revenue=None, coverage_type=None,
                      sic_code=None, employees=None, state=None, zipcode=None,
                      owner_experience=None, business_experience=None, contact_name=None,
                      contact_email=None, contact_phone=None):
    doc = frappe.get_doc({
        'doctype': 'Close Lead',
        'lead_id': lead_id,
        'contact_id': contact_id,
        'lead_name': lead_name,
        'annual_payroll': annual_payroll,
        'annual_revenue': annual_revenue,
        'coverage_type': coverage_type,
        'sic_code': sic_code,
        'employees': employees,
        'state': state,
        'zipcode': zipcode,
        'owner_experience': owner_experience,
        'business_experience': business_experience,
        'contact_name': contact_name,
        'contact_email': contact_email,
        'contact_phone': contact_phone
    })
    doc.insert()
    frappe.db.commit()
    return doc

@frappe.whitelist()
def new_payment_receipt(client=None, email=None, transaction_id=None,
                      date=None, amount=None, charge_fee=None):
    doc = frappe.get_doc({
        'doctype': 'Payment Receipt',
        'client': client,
        'email': email,
        'transaction_id': transaction_id,
        'date': date,
        'amount': amount,
        'charge_fee': charge_fee
    })
    doc.insert()
    frappe.db.commit()
    return doc
