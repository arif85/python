from modnaKastaUA.base import BasePage

class BasketPage(BasePage):

    def isJacketAdded(self):
        self.isJacketDisplayed = self.driver.find_element_by_xpath(""".//div[@class='cart_product-info']//
                                              a[@href='/product/2233244:702/?campaign=s-30633-undo-diva'][2]""")
        assert self.isJacketDisplayed is not None
        print("Jacket is present in the basket")