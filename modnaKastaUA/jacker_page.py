from selenium.webdriver.common.by import By

from modnaKastaUA.base import BasePage
from time import sleep

class JacketPage(BasePage):

    def addToBasket(self):
        self.addToBasket = self.driver.find_element_by_xpath(".//div[@class='pd_size-buttons']//div[2]//div[2]")
        self.addToBasket.click()
        print("'Dobavit d korzinu' clicked")

    def navigateToBasket(self):
        self.basketIcon = self.driver.find_element_by_xpath(".//*[@id='up']//a[@href='/basket/']")
        self.basketIcon.click()
        print("'Basket' icon clicked")

    def isJacketAdded(self):
        self.isJacketDisplayed = self.driver.find_element_by_xpath(""".//div[@class='cart_product-info']//
                                              a[@href='/product/2233244:702/?campaign=s-30633-undo-diva'][2]""")
        assert self.isJacketDisplayed is not None
        print("Jacket is present in the basket")








