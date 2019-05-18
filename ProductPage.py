import time

class ProductPage():

    def __init__(self, driver):

        self.driver = driver
        self.add_to_cart_xpath = "//button[@class='single_add_to_cart_button button alt']"
        self.view_cart_xpath = "//a[@class='button wc-forward']"


    def add_to_cart(self):
        self.driver.find_element_by_xpath(self.add_to_cart_xpath).click()
        self.driver.find_element_by_xpath(self.view_cart_xpath).click()