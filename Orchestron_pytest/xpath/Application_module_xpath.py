url = "https://staging.orchestron.dev/"

# Application 'create' button xpath's
application_tab = "//p[contains(text(),'Applications')]"
app_create_button = "//button[@id='appCreate']"
app_name = "//div[@class='modal-content']//div/input[@maxlength='50']"
app_url = "//div[2][@class='row my-1']//input"
app_platform_type = "//input[@class='el-select__input is-large']"
app_team = "//div[3][@class='row my-1']//input"
app_submit = "//button[contains(text(),'Submit')]"
app_pop_up_close_btn = "/html/body/div[1]/div/div[2]/section/div/div[2]/div/div[1]/div/div/header/button"


# Application action dropdown options xpath's
action_dropdown = "//div[contains(text(),'Actions')]"
update = "//ul[@class='el-dropdown-menu el-popper']//li[1]"
upload_results = "//ul[@class='el-dropdown-menu el-popper']//li[2]"
manual_entry = "//ul[@class='el-dropdown-menu el-popper']//li[3]"
create_view_scans = "//ul[@class='el-dropdown-menu el-popper']//li[4]"
bulk_action = "//ul[@class='el-dropdown-menu el-popper']//li[5]"
copy_webhook = "//ul[@class='el-dropdown-menu el-popper']//li[6]"
bug_tracker = "//ul[@class='el-dropdown-menu el-popper']//li[8]"
hard_mark_false_positive = "//ul[@class='el-dropdown-menu el-popper']//li[9]"
view_report = "//ul[@class='el-dropdown-menu el-popper']//li[10]"
delete = "//ul[@class='el-dropdown-menu el-popper']//li[11]"


# Manual entry pop up xpath's
man_scan_name = "//input[@maxlength='255']"
man_vul_name = "//div[@class='row my-1'][2]/div[2]/input"
man_cwe = "//div[@class='container-fluid']//div[@class='row my-1'][3]//div[2]/div"
man_owasp = "//div[@class='row my-1'][4]//input"
man_desc = "//div[@class='row my-1'][1]//textarea"
man_remed = "//div[@class='row my-1'][2]//textarea"
man_submit = "/html/body/div/div/div[2]/section/div/div[7]/div/div[1]/div/div/footer/div/div/button[2]"


# upload results xpath's
tool = "//div[@class='container-fluid']//input[@placeholder='Select']"
name = "//div[@class='container-fluid']//input[@class='inline-form-control-count-with-box orchy_font_family orchy_font_lg orchy_font_color form-control is-invalid']"
file = "//input[@accept='xml,json']"
upload_results_submit = "//button[contains(text(),'Submit')]"

# heads
open_vulnerability = "//a[contains(text(),'Opened')]"
closed_vulnerability = "//a[contains(text(),'Closed')]"
uncategorized_vulnerability = "//a[contains(text(),'Uncategorized')]"
false_positive = "//a[contains(text(),'False Positive')]"
dashboard = "//a[contains(text(),'Dashboard')]"

# closed
close_btn = "//div[contains(text(),'Close')]"
fix = "//ul[@x-placement='bottom-end']//li[2]"
wont_fix = "//ul[@x-placement='bottom-end']//li[1]"
justification = "//textarea[@placeholder='Enter Justification']"
evidence = "//input[@accept='image/jpeg, image/png,image/jpg,']"
fix_submit = "//button[contains(text(),'Submit')]"
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
