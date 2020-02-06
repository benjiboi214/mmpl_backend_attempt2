import os

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

host = os.getenv("DJANGO_EXTERNAL_HOST_NAME", "127.0.0.1")
port = os.getenv("DJANGO_EXTERNAL_PORT_NUM", "80")
protocol = os.getenv("DJANGO_EXTERNAL_PROTOCOL", "http")

opts = FirefoxOptions()
opts.add_argument("--headless")

browser = webdriver.Firefox(options=opts)
browser.get(f'{protocol}://{host}:{port}')


def test_deployment_successful():
    assert 'Page not found' in browser.title
