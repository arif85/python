from modnaKastaUA.base import BasePage
from time import sleep


class UndoDivoPage(BasePage):

    def clickHideSoldButton(self):
        self.sold = self.driver.find_element_by_xpath(".//*[@class='filter_panel']//div[@class='btn hide_sold']")
        self.sold.click()
        print("'Hide sold' clicked")

    def selectJacket(self):
        self.jacket = self.driver.find_element_by_xpath(""".//div[@class='product_item_wrap']//
                                                  a[@href='/product/2233244:702/?campaign=s-30633-undo-diva']""")
        self.jacket.click()
        print("'Undo' jacket clicked")
        sleep(1)

