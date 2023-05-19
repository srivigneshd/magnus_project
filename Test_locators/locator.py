#locators of magnus priject
class magnus_locator:
    #test case1
    temp_email_xpath="//div[@class='login-logo']//h5"
    temp_pass_xpath="//h5[text()=' Password : jobprogram ']"
    email_inputbox_xpath='(//input[@class="form-control"])[1]'
    password_inputbox_xpath='(//input[@class="form-control"])[2]'
    signin_xpath="//button[@id='btnLogin']"
    # test case 2
    employee_xpath='//ul[@id="MenusDashboard"]/li[2]'
    create_xpath="//a[normalize-space()='Create']"
    first_name_xpath="//input[@id='FirstName']"
    last_name_xpath="//input[@id='LastName']"
    email_id_xpath="//input[@id='EmailId']"
    mobile_num_xpath="//input[@id='MobileNo']"
    dob_xpath="//input[@id='DOB']"
    gender_xpath="//input[@id='rdbMale']"
    address_xpath='//textarea[@id="Address"]'
    coountry_xpath="//select[@id='CountryId']"
    city_xpath="//select[@id='CityId']"
    qa_automation_xpath="//input[@id='chkSkill_1']"
    create_save_xpath="//button[@class='btn btn-success m-r-xs']"
    #test case 3
    more_menu_xpath="//ul[@class='sidebar-menu tree leftsidemenu']/li[3]"
    multiple_table_xpath="//ul[@class='sidebar-menu tree leftsidemenu']/li[3]/descendant::a"
    