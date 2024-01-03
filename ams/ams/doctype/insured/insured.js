// // Copyright (c) 2023, JMG and contributors
// // For license information, please see license.txt

// frappe.provide("jmg");


// jmg.InsuredController = class InsuredController extends frappe.ui.form.Controller {

//     setup() {}

//     onload() {}

//     refresh() {
//         var me = this;
//         let doc = this.frm.doc;

//         frappe.dynamic_link = {
//             doc: doc,
//             fieldname: 'name',
//             doctype: 'Insured'
//         };


//         if (!this.frm.is_new()) {
//             frappe.contacts.render_address_and_contact(this.frm);
//         }
//         else {
//             frappe.contacts.clear_address_and_contact(this.frm);
//         }

//     }
// }

// extend_cscript(cur_frm.cscript, new jmg.InsuredController({ frm: cur_frm }));

// frappe.ui.form.on("Insured", {
//     // 	refresh () {

//     // 		if (!this.frm.is_new()) {
//     // 			frappe.contacts.render_address_and_contact(this.frm);
//     // 		} else {
//     // 			frappe.contacts.clear_address_and_contact(this.frm);
//     // 		}

//     // 	},
// });
