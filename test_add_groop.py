# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_groop(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_groop(self):
        success = True
        wd = self.wd
        wd.get("http://brainacad.demo.site/english/")
        wd.find_element_by_link_text("ACCOUNT").click()
        wd.find_element_by_link_text("Log In").click()
        wd.find_element_by_id("pass").click()
        wd.find_element_by_id("pass").send_keys("\\undefined")
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").send_keys("\\undefined")
        wd.find_element_by_id("send2").click()
        wd.find_element_by_link_text("ACCOUNT").click()
        wd.find_element_by_link_text("Log Out").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
