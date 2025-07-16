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
URL = "https://www.daraz.com.bd/"


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

@pytest.mark.usefixtures("setup")
class TestByChainedLocator:
    def test_chained_locator(self, setup):
        try:
            topHeader = self.driver.find_element(By.ID, "topActionHeader")
            header_content = topHeader.find_element(By.CLASS_NAME, "lzd-header-content")
            header_links = header_content.find_element(By.CLASS_NAME, "lzd-links-bar")
            header_link_lists = header_links.find_element(By.CLASS_NAME, "links-list")
            header_link_lists_item = header_link_lists.find_element(By.ID, "topActionCustomCare")
            final_text = header_link_lists_item.find_element(By.TAG_NAME, "span")
            print(final_text.text)
            time.sleep(2)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")



