import unittest
from modnaKastaUA.mainpagelogin import MainPage
from modnaKastaUA.undodivopage import UndoDivoPage
from modnaKastaUA.basetestcase import BaseTestCase
from modnaKastaUA.jackerpage import JacketPage
from modnaKastaUA.basketpage import BasketPage

class TestBaksetOnModnaKasta(BaseTestCase):

    def test_basket_on_modnaKasta(self):
        mainpage = MainPage(self.driver)
        mainpage.clickLoginButton()
        mainpage.inputEmail('mailfortestingp@ukr.net')
        mainpage.inputPassword('pythontestqweasd')
        mainpage.clickVHOD()
        mainpage.clickForMen()
        mainpage.clickUndoDivo()
        undodivopage = UndoDivoPage(self.driver)
        undodivopage.clickHideSoldButton()
        undodivopage.selectJacket()
        jacketpage = JacketPage(self.driver)
        jacketpage.addToBasket()
        jacketpage.navigateToBasket()
        basketpage = BasketPage(self.driver)
        basketpage.isJacketAdded()


    if __name__ == "__main__":
        unittest.main()
