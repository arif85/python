from modnaKastaUA.base import BasePage
from time import sleep


class MainPage(BasePage):

      def clickLoginButton(self):
          self.vhod = self.driver.find_element_by_xpath(".//div[@class='header-top_login']")
          self.vhod.click()
          print("Vhod clicked")

      def input_email(self, email):
          self.email = self.driver.find_element_by_id('username')
          self.email.clear()
          self.email.send_keys(email)
          print("Email inputed")

      def input_password(self, password):
          self.password = self.driver.find_element_by_xpath(".//form[@class='popup__left-form']//input[@id='password']")
          self.password.clear()
          self.password.send_keys(password)
          print("Password inputed")

      def clickVHOD(self):
          self.submitButton = self.driver.find_element_by_xpath(".//input[@class='popup__left-form-enter']")
          self.submitButton.click()
          print("Vhod button clicked")
          sleep(1)



      def click_for_men(self):
          self.click_for_men = self.driver.find_element_by_xpath(".//a[@href='/f/male/']")
          self.click_for_men.click()
          print("For Men clicked")


      def click_undo_divo(self):
           self.undo_divo = self.driver.find_element_by_xpath(".//a[@href='/campaign/s-30633-undo-diva/f/male/']")
           self.undo_divo.click()
           print("Undo, Divo clicked")


