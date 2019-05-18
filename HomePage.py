class HomePage():

    def __init__(self, driver):

        self.driver = driver
        self.practice_site_xpath = "//a[contains(text(),'Practice Site')]"


    def practice_site(self):
        self.driver.find_element_by_xpath(self.practice_site_xpath).click()