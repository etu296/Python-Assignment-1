import time
import pytest
from selenium import webdriver



SUPPORTED_BROWSERS = ["chrome", "firefox", "safari"]
DEFAULT_BROWSER = "chrome"
URL = "https://testing-and-learning-hub.vercel.app/index.html"

@pytest.fixture(scope="class")
def setup(request, browser=DEFAULT_BROWSER):
    if browser not in SUPPORTED_BROWSERS:
        raise ValueError(f"Browser '{browser}' is not supported")

    driver = get_webdriver(browser)
    driver.maximize_window()
    driver.get(URL)

    request.cls.driver = driver
    yield
    driver.quit()

def get_webdriver(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")


    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
    elif browser == "safari":
        options = webdriver.SafariOptions()

@pytest.mark.usefixtures("setup")
class TestBrowser:
    def test_browser(self):
        try:
            time.sleep(2)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")




