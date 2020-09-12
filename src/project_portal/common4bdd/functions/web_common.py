"""
Module containing common functions used across tests
"""
import logging as log
from selenium import webdriver

def go_to(context, url, browser_type=None):
    """
    :param url: url to navigate to
    :param browser_type: type of browser (Default is chrome)
    :return: driver webdriver instance
    """
    if not browser_type:
        context.driver = webdriver.Chrome()
    else:
        if 'chrome' == browser_type.lower():
            context.driver = webdriver.Chrome()
        elif 'firefox' == browser_type.lower():
            context.driver = webdriver.Firefox()
        else:
            raise Exception('Browser type {} not supported'.format(browser_type))
    url = url.strip()
    context.driver.get(url)
    return context.driver

def assert_element_exists(context, id):
    log.info('check is there element with id:{} on page'.format(id))
    assert context.driver.find_element_by_id(id)



