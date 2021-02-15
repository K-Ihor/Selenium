from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def test_element_by_xpath(choice_browser):
    choice_browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/h4/a").click()
    choice_browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/ul[1]/li[4]/a/img").click()
    time.sleep(5)
    choice_browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/button").click()


def test_element_by_class_name_selector(choice_browser):
    br = choice_browser
    br.find_element_by_class_name("pull-left").click()
    br.find_element_by_name("EUR").click()
    time.sleep(5)


def test_input(choice_browser):
    br = choice_browser
    br.find_element_by_name("search").send_keys("Mac")
    br.find_element_by_xpath("/html/body/header/div/div/div[2]/div/span/button").click()
    time.sleep(5)


def test_element_by_link_text(choice_browser):
    components_link = choice_browser.find_element_by_link_text("Components")
    ActionChains(choice_browser).move_to_element(components_link).pause(2).perform()
    choice_browser.find_element_by_link_text("Show All Components").click()
    time.sleep(5)


# def test_elements_by_css_celector(choice_browser):
#     navbar_items = choice_browser.find_elements(MainPage.nav_links)
#     for item in navbar_items:
#         ActionChains(choice_browser).move_to_element(item).pause(1).perform()
#     time.sleep(5)


def test_input_and_submit(browser):
    browser.find_element_by_class_name("caret").click()
    browser.find_element_by_link_text("Login").click()
    browser.find_element_by_id("input-email").send_keys("d12d17d17@gmail.com")
    browser.find_element_by_id("input-password").send_keys("admin", Keys.ENTER)
    time.sleep(5)


def test_find_by_css(browser):  # https://habr.com/ru/company/otus/blog/350368/ - написание css селекторов
    '''
    button[type=‘submit’].button_submit   #
      тег   атрибут        класс          id
    '''
    browser.find_element_by_css_selector('.product-layout img[title="iPhone"]').click()
    browser.find_element_by_css_selector(".btn#button-cart").click()
    time.sleep(2)
    browser.find_element_by_css_selector("#cart-total").click()
    browser.find_element_by_css_selector(".text-right a strong").click()
    time.sleep(2)
    assert browser.title == 'Shopping Cart'




# a[href^=“https:”] — найдет все ссылки, которые начинаются с https,
# a[href$=“.pdf”] — найдет все ссылки, которые заканчиваются на .pdf.








