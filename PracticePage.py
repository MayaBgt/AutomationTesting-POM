import time

class PracticePage():

    def __init__(self, driver):

        self.driver = driver
        self.product_xpath = "//h3[contains(text(),'Selenium Ruby')]"


    def select_product(self):
        self.driver.execute_script("window.scrollBy(0,750)", "")
        time.sleep(5)
        self.driver.find_element_by_xpath(self.product_xpath).click()