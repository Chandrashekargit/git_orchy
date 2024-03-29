# Engagement 'create' button xpath's
engagement_tab = "//a[@href='/engagements/']//p"
eng_create_btn = "//button[contains(text(), 'Create')]"
eng_create_btn2 = "//u[contains(text(),'Click here to create an Engagement or click on Create button.')]"
eng_name = "//input[@maxlength='50']"
eng_desc = "//div[@class='col-sm-12']//textarea"
eng_app_dropdown = "//input[@placeholder='Select']"
eng_bucket_type = "/html/body/div[2]/div[1]/div/div/div/div/form/div/div[2]/div[1]/div/div/div[1]/input"
dast_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='DAST']",
sast_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='SAST']",
sca_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='SCA']",
manual_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='Manual']",
script_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='Script']",
orchy_json_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='Orchestron JSON']",
infra_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='INFRA']",
container_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='Container']",
cloud_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='Cloud']",
all_bucket_type = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li/span[.='All']"
eng_date_btn = "//input[@placeholder='Select Date Range']"
eng_date1 = "//div[@class='mx-calendar'][1]//td[@class='curMonth today']"
eng_submit = "//button[contains(text(),'Submit')]"
eng_success_msg = "//p[text()='Engagement has been created successfully!']"
wrng_msg_for_same_eng_name = "//p[text()=' * engagement with this name already exists.']"
create_eng_popup_close = "//button[@aria-label='Close']"
create_eng_popup_close2 = "//button[contains(text(),'Close')]"

# Engagement heads
assign_unassign_xpath = "//a[text()='Assign / Unassign Scans']"
assign_scan_submit = "//i[@class='el-icon-arrow-right']"
unassign_scan_submit = "//i[@class='el-icon-arrow-left']"
assign_success_msg = "//p[text()='The scans have been assigned successfully!']"
unassign_success_msg = "//p[text()='The scans have been unassigned successfully!']"

# severity section
severity_section = "//a[.='Severity']"
high_severity = "//span[@class='high_badge']"
medium_severity = "//span[@class='medium_badge']"
low_severity = "//span[@class='low_badge']"
info_severity = "//span[@class='info_badge']"

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

# sections
dashboard_section = "//a[.='Dashboard']"
scans_section = "//a[.='Scans']"
vulnerabilities_section = "//a[.='Vulnerabilities']"
assign_unassign_section = "//a[.='Assign / Unassign Scans']"
