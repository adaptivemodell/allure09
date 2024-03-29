import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываю главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s('[data-target="qbsearch-input.inputButtonText"]').click()
        s('[name="query-builder-test"]').send_keys("eroshenkoam/allure-example")
        s('[name="query-builder-test"]').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s('[data-tab-item="i1issues-tab"]').click()

    with allure.step("Проверяем наличие Issue с номером 84"):
        s(by.partial_text("#84")).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tub()
    should_see_issue_with_number("#84")

@allure.step("Открываю главную страницу")
def open_main_page():
    browser.open("https://github.com")

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s('[data-target="qbsearch-input.inputButtonText"]').click()
    s('[name="query-builder-test"]').send_keys(repo)
    s('[name="query-builder-test"]').submit()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step("Открываем таб Issues")
def open_issue_tub():
    s('[data-tab-item="i1issues-tab"]').click()

@allure.step("Проверяем наличие Issue с номером 84")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()