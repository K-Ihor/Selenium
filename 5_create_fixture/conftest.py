import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://127.0.0.1/opencart/")  # pytest -s --url http://google.com - передаем в командную строку такую команду
    parser.addoption("--browser", action="store", default="chrome")  # pytest -v --browser firefox передаем в командную строку такую команду


@pytest.fixture(params=["chrome", "firefox"])  # фкс-ра для двух браузеров но можно передать опционально url
def browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")

    # driver.implicitly_wait(20)  # ждет 20 сек
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))

    return driver


@pytest.fixture  # фкс-ра для двух браузеров в которой есть выбор браузера путем передачи агрумента --browser
def choice_browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")

    # driver.implicitly_wait(20)  # ждет 20 сек
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))

    return driver