import time


def test_open_browsers(browser):
    # browser.get("http://127.0.0.1/opencart/")  # закометил эту строку так как передал по умолчанию в фикстуру опционально эту ссылку
    time.sleep(5)
    assert browser.title == "Your Store"



