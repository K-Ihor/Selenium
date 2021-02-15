from TEST_PageObject.page_objects import MainPage, ProductPage, UserPage, CartPage


def test_add_to_wish_list(browser):
    product_name = MainPage(browser).get_featured_product_name(1)
    MainPage(browser).click_featured_product(1).add_to_wishlist().alert.click_login()
    UserPage(browser).login_user(email="d12d17d17d17@gmail.com", password="password").open_wishlist().verify_product(product_name)


def test_add_to_cart(browser):
    product_name = MainPage(browser).get_featured_product_name(3)
    MainPage(browser).click_featured_product(3)
    ProductPage(browser).add_to_cart().alert.click_to_cart()
    CartPage(browser).verify_product(product_name).checkout()
    UserPage(browser).login_user(email="d12d17d17d17@gmail.com", password="password").verify_payment_form()

















