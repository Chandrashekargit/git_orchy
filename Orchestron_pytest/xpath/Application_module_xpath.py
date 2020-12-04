url = "https://graphs.orchestron.dev/"

# Application 'create' button xpath's
application_tab = "//p[contains(text(),'Applications')]"
app_create_button = "//button[contains(text(),'Create')]"
app_name = "//div[@class='modal-content']//div/input[@maxlength='50']"
app_url = "//div[2][@class='row my-1']//input"
app_platform_type = "//input[@class='el-select__input is-large']"
app_team = "//div[3][@class='row my-1']//input"
app_submit = "//button[contains(text(),'Submit')]"
app_pop_up_close_btn = "//button[@aria-label='Close']"
existing_application_warning_msg = "//p[contains(text(),' * Application with this name already exists.')]"
invalid_url_wrng_msg = "//p[contains(text(),' * Enter a valid URL.')]"
success_msg_for_app_created = "//p[text()='Application has been created successfully!']"
warning_msg_for_existing_app = "//p[.=' * Application with this name already exists.']"
success_msg_for_app_delete = "//p[.= 'Application has been deleted successfully!']"

# search field xpath
search = "//input[@placeholder='Search']"

# update application pop up
update_app_name = "//input[@class='inline-form-control-count-with-box orchy_font_family orchy_font_md orchy_font_color form-control' and @maxlength]"
update_url = "//div[@class='modal-content']//div[@class='modal-body']//div[@class='row my-1'][2]/div[1]//input"
update_name_warning_msg = "//p[text()=' * Ensure this field has no more than 50 characters.']"
update_url_warning_msg = "//p[text()=' * Enter a valid URL.']"
update_submit_btn = "//button[contains(text(),'Submit')]"
update_success_msg = "//p[.='Application has been updated successfully!']"

# Application action dropdown options xpath's
action_dropdown = "//div[contains(text(),'Actions')]"
update = "//ul[@class='el-dropdown-menu el-popper']//li[1]"
upload_results = "//ul[@class='el-dropdown-menu el-popper']//li[2]"
manual_entry = "//ul[@class='el-dropdown-menu el-popper']//li[3]"
view_scans = "//ul[@class='el-dropdown-menu el-popper']//li[4]"
bulk_action = "//ul[@class='el-dropdown-menu el-popper']//li[5]"
copy_webhook = "//ul[@class='el-dropdown-menu el-popper']//li[6]"
bug_tracker = "//ul[@class='el-dropdown-menu el-popper']//li[8]"
hard_mark_false_positive = "//ul[@class='el-dropdown-menu el-popper']//li[9]"
view_report = "//ul[@class='el-dropdown-menu el-popper']//li[10]"

# Manual entry pop up xpath's
man_scan_name = "//div[@class='row my-1']//div[@class='col-sm-12'][1]//input"
severity = "//div[@class='row my-1']//div[@class='col-sm-12'][2]//input"
man_cwe = "//div[@class='row my-1']//div[@class='col-sm-12'][3]//input"
man_desc = "//div[@class='row my-1']//div[@class='col-sm-12'][4]//input"
man_submit = "//button[contains(text(), 'Submit')]"
success_msg_for_manual_vul_creation = "//p[text()='Manual vulnerability has been created successfully!']"
empty_field_wrng_msg = "//p[.=' * This field may not be blank.']"
warning_msg_for_severity_field_empty = "//p[.=' * Please select the severity']"
warning_msg_for_cwe_field_empty = "//p[.=' * A valid integer is required.']"
close_create_manual_vul_pop_up = "//button[.='×']"

# upload results xpath's
tool = "//div[@class='container-fluid']//input[@placeholder='Select']"
name = "//input[@maxlength='100']"
file = "//input[@accept='xml,json']"
upload_results_submit = "//button[contains(text(),'Submit')]"
warning_msg_for_file_format = "//label[.=' * Supported formats are json']"
close_upload_results_pop_up = "//button[.='×']"
wrng_msg_for_same_scan_name = "//p[text()=' * Scan name should be unique']"
wrng_msg_when_we_upload_wrong_file = "//label[.=' * Not a ZAP 2.9.0 file']"
wrng_msg_for_existing_scan_name = "//p[text()=' * Scan name should be unique']"
wrng_msg_for_max_char_in_scanname_field = "//p[.=' * Ensure this field has no more than 100 characters.']"

# heads
open_vulnerability = "//a[.='Opened']"
closed_vulnerability = "//a[.='Closed']"
uncategorized_vulnerability = "//a[contains(text(),'Uncategorized')]"
false_positive = "//a[contains(text(),'False Positive')]"
dashboard = "//a[contains(text(),'Dashboard')]"

# opened_vul
basic_info = "//a[text()='Basic Info']"
vulnerability_info = "//a[text()='Vulnerability Info']"
affected_instance = "//a[text()='Affected Instances']"
vul_info = "//a[.='Vulnerability Info']"
examples = "//a[text()='Examples']"
close_evdience = "//ul[@x-placement='bottom-end' or @x-placement='top-end']//li[text()='Close evidence']"

# closed
close_btn = "//div[contains(text(),'Close')]"
fix = "//ul[@x-placement='bottom-end']//a[2]/li/li"
wont_fix = "//ul[@x-placement='bottom-end']//li[1]"
justification = "//textarea[@placeholder='Enter Justification']"
evidence = "//input[@accept='image/jpeg, image/png,image/jpg,']"
fix_vul_submit = "//button[contains(text(),'Submit')]"
reopen_btn = "//button[text()='ReOpen']"
reopen_submit = "//button[contains(text(),'Submit')]"

# PerPage drop-down xpath's
PerPageDropdown = "//input[@placeholder='Per Page']"
five = "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[1]//span[text()='5']"
ten = "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[2]//span[text()='10']"
twenty_five = "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[3]//span[text()='25']"
fifty = "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[4]//span[text()='50']"
hundered = "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[5]//span[text()='100']"
all = "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[6]//span[text()='All']"

# Delete application
delete_option = "//ul[@class='el-dropdown-menu el-popper']//li[11]"
yes = "//button[contains(text(),'Yes')]"
no = "//button[contains(text(),'No')]"
enter_delete = "//input[@placeholder='Type DELETE']"
delete = "//footer[@class='modal-footer']//button[contains(text(),'Delete')]"
cancel = "//footer[@class='modal-footer']//button[contains(text(),'Cancel')]"

# Evidence
create_evidence_btn = "//button[contains(text(), 'Create Evidence')]"
close_evd_pop_up = "//button[.='×']"
evd_justification = "//textarea[@placeholder='Enter Justification']"
evd_submit = "//button[contains(text(),'Submit')]"
success_msg_when_evd_marked_as_TP = "//p[.='Evidence successfully marked as True Positive!']"
success_msg_when_vul_marked_as_FP = "//p[.='Vulnerability successfully marked as False Positive!']"
success_msg_when_evd_marked_as_FP = "//p[.='Evidence successfully marked as False Positive!']"
reopen_evd = "//ul[@x-placement]//a//li[.='Reopen']"
success_msg_when_evd_reopened = "//p[.='Evidence successfully reopened!']"

# sast evd
sast_toggle_btn = "//div[@class='row']//div[@class='col-sm-4 col-md-4 col-4'][1]//span"
line_no_xpath = "//input[@placeholder='Enter line no']"
line_range_xpath = "//input[@placeholder='Enter line range']"
# code_snippet_xpath = "//label[@class='custom-file-label']"
code_snippet_xpath = "/html/body/div[2]/div[1]/div/div/div/div/form/div/div/div/div[4]/div[3]/div[2]/div/input"
path_xpath = "//input[@placeholder='Enter path']"
file_name_xpath = "//input[@placeholder='Enter file name']"
param_xpath = "//input[@placeholder='Enter param']"
wrng_msg_for_empty_line_no = "//p[.=' * A valid integer is required.']"
code_snippet_wrng_msg_for_empty_field = "//p[.=' * The submitted data was not a file. Check the encoding type on the form.']"
code_snippet_wrng_msg_for_invalid_file = "//p[.=' * Please upload only text files']"
wrng_msg_when_line_no_reaches_max_char = "//p[.='* Line number cannot exceed more than 5 digits']"
wrng_msg_when_line_range_reaches_max_char = "//p[.='* Ensure this field has no more than 15 characters.']"
wrng_msg_when_path_field_reaches_max_char = "//p[.='* Ensure this field has no more than 120 characters.']"
wrng_msg_when_file_field_reaches_max_char = "//p[.='* Ensure this field has no more than 12 characters.']"
wrng_msg_when_param_field_reaches_max_char = "//p[.='* Ensure this field has no more than 12 characters.']"

# dast evd
dast_toggle_btn = "//div[@class='row']//div[@class='col-sm-4 col-md-4 col-4'][2]//span"
url_xpath = "//input[@placeholder='Enter URL']"
dast_param_xpath = "//input[@placeholder='Enter param']"
payload_xpath = "//input[@placeholder='Enter payload']"
request_xpath = "/html/body/div[2]/div[1]/div/div/div/div/form/div/div/div/div[4]/div[4]/div[2]/div/input"
response_xpath = "/html/body/div[2]/div[1]/div/div/div/div/form/div/div/div/div[4]/div[5]/div[2]/div/input"
param_payload_reaching_max_char = "//p[.=' * Ensure this field has no more than 12 characters.']"
req_res_wrng_msg_for_empty_fields = "//p[.=' * The submitted data was not a file. Check the encoding type on the form.']"
req_res_wrng_msg_for_invalid_files = "//p[.=' * Please upload only text files']"

# sca evd
sca_toggle_btn = "//div[@class='row']//div[@class='col-sm-4 col-md-4 col-4'][3]//span"
module_xpath = "//input[@placeholder='Enter module']"
version_xpath = "//input[@placeholder='Enter version']"
cve_xpath = "//input[@placeholder='Enter cve']"
evd_submit = "//button[contains(text(),'Submit')]"
evd_success_msg = "//p[text()='Evidence created successfully.']"
version_id_wrng_msg = "//p[.=' * Ensure this field has no more than 12 characters.']"
cve_id_wrng_msg = "//p[.=' * Ensure this field has no more than 20 characters.']"

wrng_msg_when_fields_are_empty = "//div[@class='row']//p[.=' * This field may not be blank.']"
empty_file_wrng_msg = "//p[.=' * The submitted file is empty.']"

# Bulk actions
succes_msg_when_vuls_marked_as_FP_via_BA = "//p[.='The vulnerabilities have been marked as False positive successfully!']"