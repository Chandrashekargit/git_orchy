# users section xpath
users = "//p[text()='Users']"
settings_tab = "//p[contains(text(),'Settings')]"
create_btn = "//div[@class='col-2']//button[text()='Create']"
first_name = "//div/div/div/form/div[1]/div[1]/input"
last_name = "/html/body/div[2]/div[1]/div/div/div/div/form/div[1]/div[2]/input"
e_mail = "//div[@class='row'][2]//input"
user_name = "//div[@class='row'][2]//input[@maxlength]"
user_type = "//div[@class='row'][3]//input"
create_user_submit = "//button[contains(text(),'Submit')]"
users_section_action_dropdown = "//div[@id='left' and contains(text(),'Actions')]"
# action_dp_delete = "//ul[@x-placement='top-end']//li[text()='Delete']"
users_section_action_dropdown_delete = "/html/body/ul/li[3]/a/li"
delete_confirmation_yes = "//button[contains(text(),'Yes')]"
# delete_confirmation_yes = "/html/body/div[2]/div[1]/div/div/footer/div/div/button[2]"
delete_confirmation_no = "//button[contains(text(),'No')]"
users_search_field = "//input[@placeholder='Search']"
warning_msg_if_we_create_users_outside_org = "//p[contains(text(),'You are trying to create users outside organization. Please register the domain')]"
existing_email_warning_msg = "//p[contains(text(), ' * user with this email address already exists.')]"
existing_username_warning_msg = "//p[contains(text(), ' * This user name has already been added.')]"
success_msg_user_created = "//p[text()='The user has been created Successfully!']"
success_msg_user_deleted = "//p[text()='The user has been deleted Successfully!']"

# Team section xpath's.
team_section = "//h4[text()='Teams']"
create_user_btn = "//div[@class='col-1']//button[text()='Create']"
team_name = "//input[@maxlength='50']"
team_desc = "//textarea[@id='textarea1']"
create_team_submit = "//button[contains(text(), 'Submit')]"
search_field = "//input[@placeholder='Search']"
teams_section_action_dropdown = "//span[@class='el-dropdown-link el-dropdown-selfdefine']//div[2]"
warning_msg_when_we_create_existing_team = "//p[contains(text(),'Team with this name already exists.')]"
warning_msg_for_max_char_in_name_field = "//p[contains(text(),'Ensure this field has no more than 50 characters.')]"

# users_section_action_dropdown = "//div[contains(text(),'Actions')]"
update = "//ul[@class='el-dropdown-menu el-popper' and @x-placement]//a//li[.='Update']"
delete = "//ul[@x-placement]//li[2]"
confirm_delete = "//button[.='Yes']"
add_users = "//ul[@x-placement]//li[text()='Add Users']"
select_users_dp = "//div[@class='dropdown v-select searchable']//input"
select_users_submit = "//button[contains(text(),'Submit')]"
success_msg_team_created = "//p[text()='The team has been created Successfully!']"
success_msg_delete_team = "//p[text()='The team has been deleted Successfully!']"
wrng_msg_for_name_field_max_char = "//p[contains(text(), ' * Ensure this field has no more than 50 characters.')]"
wrng_msg_for_creating_existing_team = "//p[contains(text(), ' * Team with this name already exists.')]"

# Domain xpath's
domain_section = "//h4[text()='Domain Registration']"
domain_create = "//div[@class='bg_white container-fluid']//button[@id='grp_create']"
domain_name_field = "//input[@placeholder='Enter Domain']"
domain_name_submit = "//div[@class='pull-right']//button[text()='Create']"
domain_create_popup_close = "//button[.='×']"
doamin_action_dropdown = "//div[@id and contains(text(),'Actions')]"
domain_delete = "//ul[@x-placement]//li[text()='Delete']"
# domain_delete_yes = "//button[@class='btn btn-submit orchy_font_md' and (text()='Yes')]"
domain_delete_yes = "//button[.='Yes']"
domain_delete_no = "///button[.='No']"
domain_actiondp_update = "//ul[@x-placement]//li[text()='Update']"
domain_search_field = "//input[@placeholder='Search']"
warning_msg_for_same_domain_name = "//p[contains(text(),' * organization email domain configuration with this domain name already exists.')]"
warning_msg_for_delete_domain_while_user_exist = "//p[contains(text(),'User(s) with this domain configuration already exists. Please delete users to delete this domain configuration.')]"
warning_msg_if_we_update_domain_name_while_user_exist = "//p[@class='align_left error align_left orchy_font_sm orchy_font_family']/text()"
success_msg_domain_created = "//p[text()='Domain has been created Successfully']"
success_msg_domain_deleted = "//p[text()='Domain has been deleted Successfully!']"
wrng_msg_for_invalid_domain_name = "//p[contains(text(),'organization email domain configuration with this domain name already exists.')]"

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

back_btn = "//button[text()='Back']"