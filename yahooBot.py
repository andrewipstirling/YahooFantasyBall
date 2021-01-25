from selenium import webdriver
from time import sleep

USERNAME = ''
PASSWORD = ''
class fantasyBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\SeleniumBrowserDrivers\chromedriver.exe') #may need to change this path
    def login(self):
        self.driver.get('https://login.yahoo.com/?.lang=en-US&src=fantasy&.done=https%3A%2F%2Fbasketball.fantasysports.yahoo.com%2F&pspid=782202766&activity=ybar-signin')

        sleep(2)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        goog = self.driver.find_element_by_xpath('//*[@id="tpa-google-button"]')
        goog.click()
        sleep(1)

        #  email and password input
        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(USERNAME)
        next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
        next_btn.click()
        sleep(2)

        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pw_in.send_keys(PASSWORD)
        next_pw = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        next_pw.click()
        sleep(5)

    def setRoster(self):
        self.driver.execute_script("window.scrollTo(0, 400)")
        sleep(1)
        too_much_dog = self.driver.find_element_by_link_text("Too Much Dog")
        too_much_dog.click()
        sleep(1)

        start_players = self.driver.find_element_by_link_text("Start Active Players")
        start_players.click()
        sleep(0.5)

        week = self.driver.find_element_by_link_text("Start")
        week.click()
