import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        root_project_dir = os.path.dirname(os.path.dirname(os.getcwd()))
        self.index_html_path = "file://" + os.path.join(root_project_dir, "app/index.html")

    def test_title(self):
        self.driver.get(self.index_html_path)

        self.assertEqual(self.driver.title, "Калькулятор")

    def test_input_field_placeholder(self):
        """ Наличие поля ввода с placeholder='Введите число'"""
        self.driver.get(self.index_html_path)
        input_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Введите число']")
        self.assertIsNotNone(input_field)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()