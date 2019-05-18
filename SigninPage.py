class SigninPage():

    def __init__(self, driver):

        self.driver = driver
        self.click_signin_xpath = "//img[@id='enterimg']"


    def click_signin(self):
        self.driver.find_element_by_xpath(self.click_signin_xpath).click()