import unittest
from modnaKastaUA.main_page_login import MainPage
from modnaKastaUA.undo_divo_page import UndoDivoPage
from modnaKastaUA.basetestcase import BaseTestCase
from modnaKastaUA.jacker_page import JacketPage

class TestBaksetOnModnaKasta(BaseTestCase):

    def test_basket_on_modnaKasta(self):
        main_page = MainPage(self.driver)
        main_page.clickLoginButton()
        main_page.input_email('mailfortestingp@ukr.net')
        main_page.input_password('pythontestqweasd')
        main_page.clickVHOD()
        main_page.click_for_men()
        main_page.click_undo_divo()
        undo_divo_page = UndoDivoPage(self.driver)
        undo_divo_page.clickHideSoldButton()
        undo_divo_page.selectJacket()
        jacketpage = JacketPage(self.driver)
        jacketpage.addToBasket()
        jacketpage.navigateToBasket()
        jacketpage.isJacketAdded()


    if __name__ == "__main__":
        unittest.main()
