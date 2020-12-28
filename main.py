from selenium import webdriver
import unittest
import time


class Alfaone(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"E:\Python\chromedriver_win32 (1)\chromedriver.exe")
        cls.driver.maximize_window()


    def test_homepage(self):
        self.driver.get("https://trading.alfa-one-capital.com")
        self.assertEqual("Alfa One Capital", self.driver.title, "webpage title is not matching")


    def test_regfprm(self):
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/a[1]').click()
        self.driver.find_element_by_name('first_name').send_keys('Mark1')
        self.driver.find_element_by_name('last_name').send_keys('POlo')
        self.driver.find_element_by_name('email').send_keys('mark1sw@mail.ru')
        self.driver.find_element_by_name('phone').send_keys('123345671')
        self.driver.find_element_by_name('password').send_keys('123456781')
        self.driver.find_element_by_name('password_confirmation').send_keys('123456781')
        self.driver.find_element_by_class_name('form-checkbox').click()
        #time.sleep(10)
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[8]/button').click()
        self.assertEqual("Alfa One Capital", self.driver.title, "webpage title is not matching")




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed....")


if __name__ == '__main__':
    unittest.main()

