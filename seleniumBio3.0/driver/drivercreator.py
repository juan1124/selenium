__author__ = 'ZK'
from selenium import webdriver
import os

def create_driver(driver_type):
    BASE_DIR = os.path.dirname(__file__)
    if driver_type == 'Chrome':

        chrome_driver = BASE_DIR + '/chromedriver.exe'

        os.environ['webdriver.chrome.driver'] = chrome_driver

        driver = webdriver.Chrome(chrome_driver)
        return driver

    elif driver_type == 'IE':
        ie_driver = BASE_DIR + '/IEDriverServer.exe'
        os.environ['webdriver.ie.driver'] = ie_driver
        driver = webdriver.Ie(ie_driver)
        return driver

