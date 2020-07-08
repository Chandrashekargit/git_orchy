# Engagement 'create' button xpath's
engagement_tab = "//a[@href='/engagements/']//p"
eng_create_btn = "//button[contains(text(), 'Create')]"
eng_name = "//input[@maxlength='50']"
eng_desc = "//div[@class='col-sm-12']//textarea"
eng_app_dropdown = "//input[@placeholder='Select']"
eng_bucket_type = "/html/body/div[2]/div[1]/div/div/div/div/form/div/div[2]/div[1]/div/div/div[1]/input"
eng_date_btn = "//input[@placeholder='Select Date Range']"
eng_date1 = "//div[@class='mx-calendar'][1]//td[@class='curMonth today']"
eng_submit = "//button[contains(text(),'Submit')]"
eng_success_msg = "//p[text()='Engagement has been created successfully!']"
wrng_msg_for_same_eng_name = "//p[text()=' * engagement with this name already exists.']"
create_eng_popup_close = "//button[@aria-label='Close']"

# Engagement heads
assign_unassign_xpath = "//a[text()='Assign / Unassign Scans']"
assign_scan_submit = "//i[@class='el-icon-arrow-right']"
unassign_scan_submit = "//i[@class='el-icon-arrow-left']"
assign_success_msg = "//p[text()='The scans have been assigned successfully!']"
unassign_success_msg = "//p[text()='The scans have been unassigned successfully!']"

# Engagement action dropdown options xpath's
action_dropdown = "//div[contains(text(),'Actions')]"
eng_update = "//ul[@class='el-dropdown-menu el-popper']//li[1]"
eng_viewreport = "//ul[@class='el-dropdown-menu el-popper']//li[2]"
eng_close = "//ul[@class='el-dropdown-menu el-popper']//li[3]"
eng_delete = "//ul[@class='el-dropdown-menu el-popper']//li[4]"

# Delete Engagement
confirm_delete = "//button[contains(text(),'Delete')]"
delete_success_msg = "//p[text()='Engagement has been deleted successfully.']"

# close engagement
confirm_close_eng = "//button[contains(text(),'Close')]"
close_success_msg = "//p[text()='Engagement has been closed Successfully!']"
