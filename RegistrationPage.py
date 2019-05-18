from selenium.webdriver.support.ui import Select
import time

class RegistrationPage():

    def __init__(self, driver):

        self.driver = driver
        self.first_name_xpath = "//input[@placeholder='First Name']"
        self.last_name_xpath = "//input[@placeholder='Last Name']"
        self.address_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]"
        self.email_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]"
        self.phone_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]"
        self.gender_xpath = "//label[2]//input[1]"
        self.hobbies_xpath = "//input[@id='checkbox2']"
        self.click_language_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/multi-select[1]/div[1]"
        self.select_language_xpath = "//a[contains(text(),'Arabic')]"
        self.click_skills_xpath = "//select[@id='Skills']"
        self.click_countries_xpath = "//select[@id='countries']"
        self.click_year_xpath = "//select[@id='yearbox']"
        self.click_month_xpath = "//select[@placeholder='Month']"
        self.click_day_xpath = "//select[@id='daybox']"
        self.password_xpath = "//input[@id='firstpassword']"
        self.second_password_xpath = "//input[@id='secondpassword']"
        self.click_submit_xpath = "//button[@id='submitbtn']"


    def first_name(self, first_name):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.first_name_xpath).send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element_by_xpath(self.last_name_xpath).send_keys(last_name)

    def address(self, address):
        self.driver.find_element_by_xpath(self.address_xpath).send_keys(address)

    def email(self, email):
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def phone(self, phone):
        self.driver.find_element_by_xpath(self.phone_xpath).send_keys(phone)

    def gender(self):
        self.driver.find_element_by_xpath(self.gender_xpath).click()

    def hobbies(self):
        self.driver.find_element_by_xpath(self.hobbies_xpath).click()

    def language(self):
        self.driver.find_element_by_xpath(self.click_language_xpath).click()
        self.driver.find_element_by_xpath(self.select_language_xpath).click()

    def skills(self):
        self.driver.implicitly_wait(5)
        skills = self.driver.find_element_by_xpath(self.click_skills_xpath)
        drp = Select(skills)
        drp.select_by_visible_text("AutoCAD")

    def countries(self):
        self.driver.implicitly_wait(5)
        countries = self.driver.find_element_by_xpath(self.click_countries_xpath)
        drp = Select(countries)
        drp.select_by_visible_text("American Samoa")

    def DOB(self):

        years = self.driver.find_element_by_xpath(self.click_year_xpath)
        drp = Select(years)
        drp.select_by_visible_text("1980")

        months = self.driver.find_element_by_xpath(self.click_month_xpath)
        drp = Select(months)
        drp.select_by_visible_text("May")

        days = self.driver.find_element_by_xpath(self.click_day_xpath)
        drp = Select(days)
        drp.select_by_visible_text("10")

    def password(self, password):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def second_password(self, second_password):
        self.driver.find_element_by_xpath(self.second_password_xpath).send_keys(second_password)

    def submit(self):
        self.driver.find_element_by_xpath(self.click_submit_xpath).click()
        self.driver.implicitly_wait(5)
