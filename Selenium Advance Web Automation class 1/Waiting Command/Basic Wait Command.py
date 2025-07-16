import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

SUPPORTED_BROWSERS = {"chrome", "firefox", "edge"}
DEFAULT_BROWSER = "chrome"
#URL = "https://testing-and-learning-hub.vercel.app/index.html"
URL = "https://testing-and-learning-hub.vercel.app/WebAutomation/pages/registration_form.html"


def get_webdriver(browser):
    if browser == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

@pytest.fixture(scope="class")
def setup(request, browser=DEFAULT_BROWSER):
    if browser not in SUPPORTED_BROWSERS:
        raise ValueError()
    driver = get_webdriver(browser)
    driver.get(URL)
    time.sleep(1)
    request.cls.driver = driver
    yield
    driver.quit()
#contain Xpath
@pytest.mark.usefixtures("setup")
class TestImplicitWait:
    #implicit wait
    def test_implicit_wait(self, setup):
        try:
            self.driver.implicitly_wait(30)
            self.driver.get(URL)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")