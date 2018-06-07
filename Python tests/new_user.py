# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Manufacturer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_manufacturer(self):
        driver = self.driver
        driver.get("https://test-portal.3shapecommunicate.com/#/login")
        driver.find_element_by_link_text("create new account").click()
        driver.find_element_by_link_text("I am a 3Shape software user").click()
        driver.find_element_by_name("FirstName").click()
        driver.find_element_by_name("FirstName").clear()
        driver.find_element_by_name("FirstName").send_keys("Test Lab")
        driver.find_element_by_name("LastName").click()
        driver.find_element_by_name("LastName").clear()
        driver.find_element_by_name("LastName").send_keys("Junior test")
        driver.find_element_by_name("Email").click()
        driver.find_element_by_name("Email").clear()
        driver.find_element_by_name("Email").send_keys("test2@banit.club")
        driver.find_element_by_name("Password").click()
        driver.find_element_by_name("Password").clear()
        driver.find_element_by_name("Password").send_keys("test2@banit.club")
        driver.find_element_by_name("Password-repeated").click()
        driver.find_element_by_name("Password-repeated").clear()
        driver.find_element_by_name("Password-repeated").send_keys("test2@banit.club")
        driver.find_element_by_xpath("//button").click()
        driver.find_element_by_name("Name").click()
        driver.find_element_by_name("Name").clear()
        driver.find_element_by_name("Name").send_keys("New Manufacturer Lab")
        driver.find_element_by_name("country").click()
        Select(driver.find_element_by_name("country")).select_by_visible_text("Austria")
        driver.find_element_by_xpath("//option[@value='object:450']").click()
        driver.find_element_by_name("City").click()
        driver.find_element_by_name("City").clear()
        driver.find_element_by_name("City").send_keys("Vienna")
        driver.find_element_by_name("AddressLine").clear()
        driver.find_element_by_name("AddressLine").send_keys("street")
        driver.find_element_by_name("PostalCode").clear()
        driver.find_element_by_name("PostalCode").send_keys("123")
        driver.find_element_by_name("PhoneNumber").clear()
        driver.find_element_by_name("PhoneNumber").send_keys("123")
        driver.find_element_by_xpath("//div[8]/div/div[2]/button").click()
        driver.find_element_by_name("dongleNumber").click()
        driver.find_element_by_name("dongleNumber").clear()
        driver.find_element_by_name("dongleNumber").send_keys("945390570")
        driver.find_element_by_xpath("//div[2]/div/div[2]/button").click()
        driver.find_element_by_xpath("//div[3]/div/label/span").click()
        driver.find_element_by_xpath("//div[4]/div/div[2]/button").click()
        driver.find_element_by_xpath("//div[3]/div/button").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
