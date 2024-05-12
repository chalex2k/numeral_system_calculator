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

    def test_radio_buttons_group(self):
        """ Наличие переключателей Стартовая система счисления"""
        self.driver.get(self.index_html_path)
        legend = self.driver.find_element(By.XPATH, "//fieldset/legend")
        self.assertEqual(legend.text, "Стартовая система счисления")
        expected_options = ("Двоичная", "Троичная", "Восьмеричная", "Десятичная", "Шестнадцатеричная",
                            "Пользовательская")
        for option in expected_options:
            label = self.driver.find_element(By.XPATH, f"//label[text()='{option}']")
            self.assertTrue(label.is_displayed())

    def test_custom_input_appears(self):
        """ При выборе опции пользовательская появляется поле для кастомной СС """
        self.driver.get(self.index_html_path)
        fieldset = self.driver.find_element(By.XPATH, "//fieldset[legend='Стартовая система счисления']")

        custom_radio_button = fieldset.find_element(By.ID, "custom")
        custom_radio_button.click()
        custom_input = fieldset.find_element(By.CSS_SELECTOR, "input[placeholder='Введите Вашу систему счисления']")
        self.assertTrue(custom_input.is_displayed())

    def test_custom_input_disappears(self):
        """ При выборе любых других опций поле для кастомной СС скрыто """
        self.driver.get(self.index_html_path)
        fieldset = self.driver.find_element(By.XPATH, "//fieldset[legend='Стартовая система счисления']")

        for rb in ("binary", "ternary", "octal", "decimal", "hexadecimal"):
            non_custom_radio_button = fieldset.find_element(By.ID, rb)
            non_custom_radio_button.click()
            custom_input = fieldset.find_element(By.CSS_SELECTOR, "input[placeholder='Введите Вашу систему счисления']")
            self.assertFalse(custom_input.is_displayed())

    def test_radio_buttons_group_result(self):
        """ Наличие переключателей Итоговая система счисления"""
        self.driver.get(self.index_html_path)
        legend = self.driver.find_element(By.XPATH, "//fieldset[2]/legend")
        self.assertEqual(legend.text, "Итоговая система счисления")
        expected_options = ("Двоичная", "Троичная", "Восьмеричная", "Десятичная", "Шестнадцатеричная",
                            "Пользовательская")
        for option in expected_options:
            label = self.driver.find_element(By.XPATH, f"//fieldset[2]//label[text()='{option}']")
            self.assertTrue(label.is_displayed())

    def test_custom_input_appears_result(self):
        """ При выборе опции пользовательская появляется поле для итоговой СС"""
        self.driver.get(self.index_html_path)
        fieldset = self.driver.find_element(By.XPATH, "//fieldset[2][legend='Итоговая система счисления']")

        custom_radio_button = fieldset.find_element(By.ID, "customResult")
        custom_radio_button.click()
        custom_input = fieldset.find_element(By.CSS_SELECTOR, "input[placeholder='Введите Вашу систему счисления']")
        self.assertTrue(custom_input.is_displayed())

    def test_custom_input_disappears_result(self):
        """ При выборе любых других опций поле для итоговой СС скрыто"""
        self.driver.get(self.index_html_path)
        fieldset = self.driver.find_element(By.XPATH, "//fieldset[2][legend='Итоговая система счисления']")

        for rb in ("binaryResult", "ternaryResult", "octalResult", "decimalResult", "hexadecimalResult"):
            non_custom_radio_button = fieldset.find_element(By.ID, rb)
            non_custom_radio_button.click()
            custom_input = fieldset.find_element(By.CSS_SELECTOR, "input[placeholder='Введите Вашу систему счисления']")
            self.assertFalse(custom_input.is_displayed())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
