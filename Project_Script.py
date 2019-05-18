import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from Pages.SigninPage import SigninPage
from Pages.RegistrationPage import RegistrationPage
from Pages.HomePage import HomePage
from Pages.PracticePage import PracticePage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "/Users/User/Documents/CACC/Module 5 - Automation/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_click_signin(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in")

        signinpage = SigninPage(driver)
        signinpage.click_signin()

        registration = RegistrationPage(driver)
        registration.first_name("May")
        registration.last_name("Nineth")
        registration.address("Middle of Nowhere")
        registration.email("maya.bogatskaya@gmail.com")
        registration.gender()
        registration.hobbies()
        registration.language()
        registration.skills()
        registration.countries()
        registration.DOB()
        registration.phone("5034568963")
        registration.password("Maya123456!")
        registration.second_password("Maya123456!")


        homepage = HomePage(driver)
        homepage.practice_site()

        practicepage = PracticePage(driver)
        practicepage.select_product()

        productpage = ProductPage(driver)
        productpage.add_to_cart()

        cartpage = CartPage(driver)
        cartpage.procede_to_checkout()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/User/PycharmProjects/Sel_Practice/venv/Lib/site-packages/HtmlTestRunner"),verbosity=2)

