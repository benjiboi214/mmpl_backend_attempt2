import os
import unittest

from selenium import webdriver

from webdriver_wrapper import WebDriverWrapper


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = WebDriverWrapper().driver

        self.host = os.getenv("DJANGO_EXTERNAL_HOST_NAME", "127.0.0.1")
        self.port = os.getenv("DJANGO_EXTERNAL_PORT_NUM", "80")
        self.protocol = os.getenv("DJANGO_EXTERNAL_PROTOCOL", "http")

    def tearDown(self):
        self.browser.quit()

    def _get_host_url(self):
        return f'{self.protocol}://{self.host}:{self.port}'

    def test_home_page_is_under_construction(self):
        self.browser.get(self._get_host_url())

        # Ensure Under Construction is in the title
        self.assertIn('Under Construction', self.browser.title)

    def test_404_page_is_served(self):
        self.browser.get(self._get_host_url() + "/this-does-not-exst")

        # Ensure Under Construction is in the title
        self.assertIn('Page not found', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
