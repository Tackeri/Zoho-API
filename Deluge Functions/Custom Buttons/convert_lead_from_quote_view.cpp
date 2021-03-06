// Author: MinterS
// Description: Convert Lead Button from Quote View
// Requirements: "Lead Name" Lookup on Quotes Layout
// Arguments: quoteId = Quote Id

// Declare Variables
quote_ID = quoteId.toLong();
lead_ID = "";
contact_ID = "";
account_ID = "";

// Get Lead ID from Quote
quoteDetails = zoho.crm.getRecordById("Quotes",quote_ID);
lead_name = quoteDetails.get("Lead_Name");
lead_ID = lead_name.get("id");

// Response = Convert Lead
resp = zoho.crm.convertLead(lead_ID,{"overwrite":true,"notify_lead_owner":false,"notify_new_entity_owner":true});

// Save Account / Contact ID
account_ID = resp.get("Accounts");
contact_ID = resp.get("Contacts");
quote_map = Map();
quote_map.put("Account_Name",account_ID);
quote_map.put("Contact_Name",contact_ID);

// Update Quote with Account / Contact ID
resp = zoho.crm.updateRecord("Quotes",quote_ID,quote_map);
return "Success: Lead Converted";