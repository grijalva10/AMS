// Copyright (c) 2023, JMG and contributors
// For license information, please see license.txt

frappe.ui.form.on("Transaction", {
    
    refresh(frm){
        
        console.log('oypoooo')
        
    },
    
    policies_add(frm, cdt, cdn){console.log('add')},
    policies_remove(frm, cdt, cdn){console.log('minus')},
    // policies_move(frm, cdt, cdn){console.log('move')}
    
    // set_total: function(frm) {
    //   var total_premium = 0;
    //   $.each(frm.doc.policies, function(i, d) { total_premium += d.premium; });
    //   frm.set_value("total_premium", total_premium);
    // },
    // policies_add: function(frm, ) {
    //   frm.events.set_total(frm);
    // },
    // qty: function(frm) {
    //   frm.events.set_total(frm);
    // },
});

frappe.ui.form.on("Policies", "policies_on_form_rendered", "packed_items_on_form_rendered", function(frm, cdt, cdn) {
    console.log('yooooooooooooooooooooooooooooooooo')
	// enable tax_amount field if Actual
})

// frappe.ui.form.on("policies", {
//     status(frm,cdt,cdn) {
//         let row = locals[cdt][cdn]
//         if (row.status == "Estimate"){
//             frm.set_value("status","Estimate")
//         }
//     }
// });