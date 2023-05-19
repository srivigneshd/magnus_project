from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from Test_Data.data import magnus_data
from Test_locators.locator import magnus_locator
import random
from time import sleep
import re
import pytest
 

class Test_magnus:
    #constructor with url of application
    @pytest.fixture
    def boot(self):
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
    #FROM GUI page get temp user_id and password
    # def test_userid_password_from_UI_page(self,boot):
    #     self.driver.implicitly_wait(10)
    #     self.url=magnus_data.url
    #     self.driver.maximize_window()
    #     self.driver.get(magnus_data().url)
    #     str=self.driver.find_element(by=By.XPATH,value=magnus_locator().temp_email_xpath).text
    #     actual_email_id=str[8::]
    #     pas=self.driver.find_element(by=By.XPATH,value=magnus_locator().temp_pass_xpath).text
    #     actual_password=pas[11::]
    #     email_inputbox=self.driver.find_element(by=By.XPATH,value=magnus_locator().email_inputbox_xpath)
    #     email_inputbox.clear()
    #     email_inputbox.send_keys(actual_email_id)
    #     password_inputbox=self.driver.find_element(by=By.XPATH,value=magnus_locator().password_inputbox_xpath)
    #     password_inputbox.clear()
    #     password_inputbox.send_keys(actual_password)
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().signin_xpath).click()
    #     sleep(5)
    #     assert self.driver.title=="Magnus"
        
    # def test_create_new_emp(self,boot):
    #     self.driver.implicitly_wait(10)
    #     self.url=magnus_data.url
    #     self.driver.maximize_window()
    #     self.driver.get(magnus_data().url)
    #     str=self.driver.find_element(by=By.XPATH,value=magnus_locator().temp_email_xpath).text
    #     actual_email_id=str[8::]
    #     pas=self.driver.find_element(by=By.XPATH,value=magnus_locator().temp_pass_xpath).text
    #     actual_password=pas[11::]
    #     email_inputbox=self.driver.find_element(by=By.XPATH,value=magnus_locator().email_inputbox_xpath)
    #     email_inputbox.clear()
    #     email_inputbox.send_keys(actual_email_id)
    #     password_inputbox=self.driver.find_element(by=By.XPATH,value=magnus_locator().password_inputbox_xpath)
    #     password_inputbox.clear()
    #     password_inputbox.send_keys(actual_password)
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().signin_xpath).click()
    #     sleep(5)
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().employee_xpath).click()
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().create_xpath).click()
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().first_name_xpath).send_keys(magnus_data().first_name)
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().last_name_xpath).send_keys(magnus_data().last_name)
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().email_id_xpath).send_keys(magnus_data().email_id)
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().mobile_num_xpath).send_keys(magnus_data().mobile_number)
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().dob_xpath).send_keys(magnus_data().dob)
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().gender_xpath).click()
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().address_xpath).send_keys(magnus_data().address)
    #     country=Select(self.driver.find_element(by=By.XPATH,value=magnus_locator().coountry_xpath))
    #     country.select_by_visible_text("India")
    #     city=Select(self.driver.find_element(by=By.XPATH,value=magnus_locator().city_xpath))
    #     city.select_by_visible_text("Chennai")
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().qa_automation_xpath).click()
    #     self.driver.find_element(by=By.XPATH,value=magnus_locator().create_save_xpath).click()
    #     assert self.driver.current_url=="https://magnus.jalatechnologies.com/Employee/Create"

    def test_menu_multipletable(self,boot):
        self.driver.implicitly_wait(10)
        self.url=magnus_data.url
        self.driver.maximize_window()
        self.driver.get(magnus_data().url)
        str=self.driver.find_element(by=By.XPATH,value=magnus_locator().temp_email_xpath).text
        actual_email_id=str[8::]
        pas=self.driver.find_element(by=By.XPATH,value=magnus_locator().temp_pass_xpath).text
        actual_password=pas[11::]
        email_inputbox=self.driver.find_element(by=By.XPATH,value=magnus_locator().email_inputbox_xpath)
        email_inputbox.clear()
        email_inputbox.send_keys(actual_email_id)
        password_inputbox=self.driver.find_element(by=By.XPATH,value=magnus_locator().password_inputbox_xpath)
        password_inputbox.clear()
        password_inputbox.send_keys(actual_password)
        self.driver.find_element(by=By.XPATH,value=magnus_locator().signin_xpath).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=magnus_locator().more_menu_xpath).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=magnus_locator().multiple_table_xpath).click()
        sleep(5)
        assert self.driver.title=="Magnus"
