import os

from selenium import webdriver

host = os.getenv("DJANGO_EXTERNAL_HOST_NAME", "")
port = os.getenv("DJANGO_EXTERNAL_PORT_NUM", "")

browser = webdriver.Firefox()
browser.get(f'http://{host}:{port}')

assert 'Django' in browser.title
