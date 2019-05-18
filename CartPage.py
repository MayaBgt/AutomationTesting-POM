import time

class CartPage():

    def __init__(self, driver):

        self.driver = driver
        self.checkout_xpath = "//a[@class='checkout-button button alt wc-forward']"


    def procede_to_checkout(self):
        self.driver.execute_script("window.scrollBy(0,750)", "")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.checkout_xpath).click()