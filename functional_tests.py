import os

from selenium import webdriver

host = os.getenv("DJANGO_EXTERNAL_HOST_NAME", "")
port = os.getenv("DJANGO_EXTERNAL_PORT_NUM", "")

browser = webdriver.Firefox()
browser.get(f'http://{host}:{port}')


def test_deployment_successful():
    assert 'Page not found' in browser.title
