# profile xpath's
profile_dropdown = "//img[@src='/static/img/profile_2.png']"
profile = "//li[contains(text(),'Profile')]"
firstname = "//div/div/div[2]/div[1]/div[1]/div[2]/input"
secondname = "//div/div/div[2]/div[1]/div[2]/div[2]/input"
e_mail = "//div/div/div[2]/div[1]/div[3]/div[2]/input"
submit = "//button[contains(text(),'Submit')]"
warning_message1 = "//p[text()=' * Ensure this field has no more than 30 characters.']"
email_field_warning_message1 = "//p[text()=' * Please Provide Valid Email']"
email_field_warning_message2 = "//p[text()=' * You cannot update the email! Please contact the administrator']"

# change password xpath's
change_pw_section = "//a[text()='Change your password']"
pw_rules = "//div[@class='tab-pane active']//div[@class='col-3']"
current_pw = "//div[2]/div[1]/div[1]/form/div[1]/div[2]/input"
new_pw = "//input[@type='password' and @class='form-control']"
confirm_new_pw = "//div[2]/div[1]/div[1]/form/div[3]/div[2]/input"
change_pw_submit_btn = "//div[@class='tab-pane active']//button[contains(text(),'Submit')]"
change_pw_warning_msg1 = "//p[text()=' * Old password cannot be reused!']"
change_pw_warning_msg2 = "//p[text()=' * Invalid credenetials!']"

# Logout xpath's
logout = "//span[text()='LogOut']"


