import os
import unittest
import uuid

from selenium import webdriver


class WebDriverTest(unittest.TestCase):

    def get_lambda_web_driver(self):
        chrome_options = webdriver.ChromeOptions()
        self._tmp_folder = '/tmp/{}'.format(uuid.uuid4())

        if not os.path.exists(self._tmp_folder):
            os.makedirs(self._tmp_folder)

        if not os.path.exists(self._tmp_folder + '/user-data'):
            os.makedirs(self._tmp_folder + '/user-data')

        if not os.path.exists(self._tmp_folder + '/data-path'):
            os.makedirs(self._tmp_folder + '/data-path')

        if not os.path.exists(self._tmp_folder + '/cache-dir'):
            os.makedirs(self._tmp_folder + '/cache-dir')

        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1280x1696')
        chrome_options.add_argument('--user-data-dir={}'.format(self._tmp_folder + '/user-data'))
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--log-level=0')
        chrome_options.add_argument('--v=99')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--data-path={}'.format(self._tmp_folder + '/data-path'))
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--homedir={}'.format(self._tmp_folder))
        chrome_options.add_argument('--disk-cache-dir={}'.format(self._tmp_folder + '/cache-dir'))
        chrome_options.add_argument(
            'user-agent=Mozilla/5.0 (X11; Linux x86_64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/61.0.3163.100 Safari/537.36')

        chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

        return webdriver.Chrome(chrome_options=chrome_options)

    def get_local_webdriver(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")

        return webdriver.Firefox(options=firefox_options)


class NewVisitorTest(WebDriverTest):

    def setUp(self):
        self.is_lambda_test = os.getenv("PYTEST_LAMBDA_FLAG", False)
        if self.is_lambda_test:
            self.browser = self.get_lambda_web_driver()
        else:
            self.browser = self.get_local_webdriver()

        self.host = os.getenv("DJANGO_EXTERNAL_HOST_NAME", "127.0.0.1")
        self.port = os.getenv("DJANGO_EXTERNAL_PORT_NUM", "80")
        self.protocol = os.getenv("DJANGO_EXTERNAL_PROTOCOL", "http")

    def tearDown(self):
        self.browser.quit()

    def _get_host_url(self):
        if self.is_lambda_test:
            return f'{self.protocol}://{self.host}:{self.port}'
        else:
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
