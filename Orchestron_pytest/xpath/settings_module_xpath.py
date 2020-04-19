# users section xpath
users = "//a[text()='Users']"
settings_tab = "//p[contains(text(),'Settings')]"
create_btn = "//div[@class='col-2']//button[text()='Create']"
first_name = "//div/div/div/form/div[1]/div[1]/input"
last_name = "/html/body/div[2]/div[1]/div/div/div/div/form/div[1]/div[2]/input"
e_mail = "//div[@class='row'][2]//input"
user_name = "//div[@class='row'][2]//input[@maxlength]"
user_type = "//div[@class='row'][3]//input"
create_user_submit = "//button[contains(text(),'Submit')]"
users_section_action_dropdown = "//tr[@class='el-table__row']//td[6]/div//span/div"
action_dp_delete = "//ul[@x-placement='top-end']//li[text()='Delete']"
# delete_confirmation_yes = "//button[contains(text(),'Yes')]"
delete_confirmation_yes = "/html/body/div[2]/div[1]/div/div/footer/div/div/button[2]"
delete_confirmation_no = "//button[contains(text(),'No')]"

# create team xpath's.
team_section = "//a[text()='Teams']"
create_user_btn = "//div[@class='col-1']//button[text()='Create']"
team_name = "//div[@style='padding: 7px;']/form/div[1]//div[@class='col-sm-10']/input"
team_desc = "//div[@style='padding: 7px;']/form/div[2]//div[@class='col-sm-10']/textarea"
create_team_submit = "//button[contains(text(), 'Submit')]"
search_field = "/html/body/div/div/div[2]/section/div/div[1]/div/div/div[2]/div/div/div[11]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[3]/input"
teams_section_action_dropdown = "//tr[@aria-rowindex='1']//td[@aria-colindex='4' and @data-label=' ']"
# users_section_action_dropdown = "//div[contains(text(),'Actions')]"
update = "//ul[@x-placement='top-end']//li[1]"
delete = "//ul[@x-placement='top-end']//li[2]"
add_users = "//ul[@x-placement='top-end']//li[3]"
select_users_dp = "//div[@class='dropdown v-select searchable']//input"
select_users_submit = "//button[contains(text(),'Submit')]"

# Domain xpath's
domain_section = "//a[text()='Domains']"
domain_create = "//div[@class='bg_white container-fluid']//button[@id='grp_create']"
domain_name_field = "//input[@placeholder='Enter Domain']"
domain_name_submit = "//button[@data-dismiss='createDomainModal']"
domain_create_popup_close = "//button[text()='Close']"
doamin_action_dropdown = "//table/tbody/tr[1]/td[2]/div/div/span/div/div[1]"
domain_actiondp_delete = "//ul[@x-placement='top-end']//li[text()='Delete']"
# domain_delete_yes = "//button[@class='btn btn-submit orchy_font_md' and (text()='Yes')]"
domain_delete_yes = "/html/body/div[2]/div[1]/div/div/footer/div/div/button[2]"
domain_delete_no = "//button[@class='btn btn-submit orchy_font_md' and (text()='No')]"
domain_actiondp_update = "//ul[@x-placement='top-end']//li[text()='Update']"
domain_search_field = "//div[3]/div/div/div[1]/div[3]/input"
warning_msg_for_same_domain_name = "//p[contains(text(),' * organization email domain configuration with this domain name already exists.')]"
warning_msg_for_delete_domain_while_user_exist = "//p[contains(text(),'* User with this domain configuration alredy exists please delete users if want to delete this domain configuration')]"
warning_msg_if_we_update_domain_name_while_user_exist = "//p[contains(text(),'* User with this domain configuration alredy exists please delete users if want to edit this domain configuration')]"


# vul_label_modification_and_notification
vul_label_modification_and_notification = "//a[text()='Vulnerability Label Modification and Notifications']"
severity_labels = "//a[text()='Severity Labels']"
high = "//div[@class='tab-content']//div[@class='row my-1'][1]//div[2]//input"
medium = "//div[@class='tab-content']//div[@class='row my-1'][2]//div[2]//input"
low = "//div[@class='tab-content']//div[@class='row my-1'][3]//div[2]//input"
info = "//div[@class='tab-content']//div[@class='row my-1'][4]//div[2]//input"
severity_labels_submit = "//button[contains(text(),'Submit')]"
warning_message = "//p[contains(text(),' * Ensure this field has no more than 10 characters.')]"

notification = "//a[text()='Notifications']"
application_notification = "//div[@class='list-group']//div[1]//label//div/div"
engagement_notification = "//div[@class='list-group']//div[2]//label//div/div"
scan_notification = "//div[@class='list-group']//div[3]//label//div/div"
users_notification = "//div[@class='list-group']//div[4]//label//div/div"
teams_notification = "//div[@class='list-group']//div[5]//label//div/div"

