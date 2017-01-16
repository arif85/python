import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.modnakasta.ua")
        modnaKastaTitle = "ModnaKasta"
        assert modnaKastaTitle in self.driver.title
        print("Main page loaded")

    def tearDown(self):
        self.driver.quit()
        print("Browser and page closed")