from modnaKastaUA.base import BasePage
from time import sleep


class MainPage(BasePage):

      def clickLoginButton(self):
          self.vhod = self.driver.find_element_by_xpath(".//div[@class='header-top_login']")
          self.vhod.click()
          print("Vhod clicked")

      def inputEmail(self, email):
          self.email = self.driver.find_element_by_id('username')
          self.email.clear()
          self.email.send_keys(email)
          print("Email inputed")

      def inputPassword(self, password):
          self.password = self.driver.find_element_by_xpath(".//form[@class='popup__left-form']//input[@id='password']")
          self.password.clear()
          self.password.send_keys(password)
          print("Password inputed")

      def clickVHOD(self):
          self.submitButton = self.driver.find_element_by_xpath(".//input[@class='popup__left-form-enter']")
          self.submitButton.click()
          print("Vhod button clicked")
          sleep(1)



      def clickForMen(self):
          self.clickForMen = self.driver.find_element_by_xpath(".//a[@href='/f/male/']")
          self.clickForMen.click()
          print("For Men clicked")


      def clickUndoDivo(self):
           self.undo_divo = self.driver.find_element_by_xpath(".//a[@href='/campaign/s-30633-undo-diva/f/male/']")
           self.undo_divo.click()
           print("Undo, Divo clicked")


