from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s('[data-target="qbsearch-input.inputButtonText"]').click()
    s('[name="query-builder-test"]').send_keys("eroshenkoam/allure-example")
    s('[name="query-builder-test"]').submit()

    s(by.link_text("eroshenkoam/allure-example")).click()
    s('[data-tab-item="i1issues-tab"]').click()
    s(by.partial_text("#84")).should(be.visible)
