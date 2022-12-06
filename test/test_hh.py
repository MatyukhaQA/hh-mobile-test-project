import os

import allure
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selene import have
from selene.support.conditions import be
from selene.support.shared import browser

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@allure.tag('mobile')
def test_job_search():
    browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close')) \
        .click()
    browser.element((AppiumBy.ID, 'ru.hh.android:id/view_main_search_text_view_position')).click()
    browser.element((AppiumBy.ID, 'ru.hh.android:id/toolbar_search_query')).send_keys('QA automation')
    browser.element((AppiumBy.ID, 'ru.hh.android:id/cell_compound_left_image_title_text_view_title')).click()

    browser.element((AppiumBy.ID, 'ru.hh.android:id/cell_vacancy_card_button_response')) \
        .should(have.text('Откликнуться'))
    browser.element((AppiumBy.ID, 'ru.hh.android:id/cell_vacancy_card_text_view_job_position')).should(have.text('QA'))
    browser.element((AppiumBy.ID, 'ru.hh.android:id/cell_vacancy_card_text_view_job_position')) \
        .should(have.text('Automation'))


@allure.tag('mobile')
def test_login():
    browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="У меня есть аккаунт. Войти"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="По телефону или почте"]')).click()
    browser.element((AppiumBy.ID, 'ru.hh.android:id/view_line_input_edit_text')).send_keys(LOGIN)
    browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_authorization_by_code_text_view_to_login_by_password'))\
        .click()
    browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_native_auth_edit_text_password')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.EditText[@text="Пароль"]')).send_keys(PASSWORD)
    browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_native_auth_button_enter')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Профиль"]')).click()

    browser.element((AppiumBy.ID, 'ru.hh.android:id/view_item_profile_header_text_view_position'))\
        .should(have.text('QA automation'))
    browser.element((AppiumBy.ID, 'ru.hh.android:id/view_resume_profile_statistics_text_title'))\
        .should(have.text('Статистика за неделю'))


@allure.tag('mobile')
def test_information_about_app():
    browser.element(
        (AppiumBy.ID, 'ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.FrameLayout[5]')).click()
    browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_resume_list_container_burger_button')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="O приложении"]')).click()

    browser.element((AppiumBy.CLASS_NAME, 'android.widget.ScrollView')).should(be.visible)
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Версия: 7.2"]')).should(have.text('Версия: 7.2'))
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Оценить приложение"]')) \
        .should(have.text('Оценить приложение'))


@allure.tag('mobile')
def test_main_page():
    browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close'))\
        .click()

    browser.element((AppiumBy.CLASS_NAME, 'android.view.ViewGroup')).should(be.visible)
    browser.element((AppiumBy.ID, 'ru.hh.android:id/cell_section_header_large_narrow_text_view')) \
        .should(have.text('Вакансии для вас'))
    assert len(browser.elements((AppiumBy.ID, 'ru.hh.android:id/bottom_navigation_container'))) == 5


@allure.tag('mobile')
def test_view_vacancy():
    browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_intentions_onboarding_choose_direction_image_close'))\
        .click()
    browser.element((AppiumBy.ID, 'ru.hh.android:id/cell_vacancy_card_text_view_location')).click()

    browser.element((AppiumBy.ID, 'ru.hh.android:id/menu_vacancy_info_hidden_add')).should(be.visible)
    browser.element((AppiumBy.ID, 'ru.hh.android:id/menu_vacancy_info_share')).should(be.visible)
    browser.element((AppiumBy.ID, 'ru.hh.android:id/menu_vacancy_info_favorite_add')).should(be.visible)
    browser.element((AppiumBy.ID, 'ru.hh.android:id/view_hh_button_title_subtitle_text_view_title')) \
        .should(have.text('Откликнуться'))
