import logging as log

from functions import web_common
from behave import given, then, step

log.basicConfig(level='INFO')


@given('I go to the site {url}')
def go_to_url(context, url):
    """
    Step definition to go to site
    :param context:
    :param url: url of site to go
    """
    log.info(f'Navigating to {url}')
    context.driver = web_common.go_to(context, url)


@step('page should have element with id {id}')
def page_has_element_with_id(context, id):
    log.info(f'check has page id {id}')
    web_common.assert_element_exists(context, id)
