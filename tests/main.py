import os
import unittest
from selenium import webdriver


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        root_project_dir = os.path.dirname(os.path.dirname(os.getcwd()))
        self.index_html_path = "file://" + os.path.join(root_project_dir, "app/index.html")

    def test_title(self):
        self.driver.get(self.index_html_path)

        self.assertEqual(self.driver.title, "Калькулятор")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
