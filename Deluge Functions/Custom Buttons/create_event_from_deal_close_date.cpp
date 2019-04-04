// Author: MinterS
// Description: Create Event from Deal View
// Requirements: "Close Date" value on Deal
// Arguments: dealId = Deal Id

DealDetails = zoho.crm.getRecordById("Deals",dealId);
startdate = ifnull(DealDetails.get("Closing_Date"),"").toString("yyyy-MM-dd");
enddate = ifnull(DealDetails.get("Closing_Date"),"").toString("yyyy-MM-dd");
eventmap = Map();
eventmap.put("Event_Title",ifnull(DealDetails.get("Deal_Name"),""));
eventmap.put("Who_Id",ifnull(DealDetails.get("Contact_Name"),"").get("id"));
eventmap.put("Owner",ifnull(DealDetails.get("Owner"),"").get("id"));
eventmap.put("What_Id",dealId);
eventmap.put("$se_module","Deals");
eventmap.put("Start_DateTime",startdate + "T00:00:00+00:00");
eventmap.put("End_DateTime",enddate + "T23:59:59+00:00");
eventmap.put("All_day",true);
createEvent = zoho.crm.createRecord("Events",eventmap);
info eventmap;
info createEvent;