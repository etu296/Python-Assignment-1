import pytest
import time
from selenium import webdriver
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
# Find Locator By ID
@pytest.mark.usefixtures("setup")
class TestLocatorById:
    def test_find_by_id(self):
        try:
            username = self.driver.find_element(By.ID, "loginEmail")
            username.send_keys("etu")
            time.sleep(3)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")
# By Class Name
@pytest.mark.usefixtures("setup")
class TestLocatorByClassName:
    def test_find_by_class_name(self):
        try:
            button = self.driver.find_element(By.CLASS_NAME, "btn")
            button.click()
            time.sleep(3)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")
# By Name
@pytest.mark.usefixtures("setup")
class TestLocatorByName:
    def test_locator_by_name(self):
        try:
            username = self.driver.find_element(By.NAME, "first-name")
            username.send_keys("era")
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")
# By tag name
@pytest.mark.usefixtures("setup")
class TestLocatorByTagName:
    def test_locator_by_tag_name(self):
        try:
            element = self.driver.find_elements(By.TAG_NAME, "input")
            print(f"Number of Input Tags: {len(element)}")
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")
# By Link text
@pytest.mark.usefixtures("setup")
class TestLocatorByLinkText:
    def test_locator_by_link_text(self):
        try:
            element = self.driver.find_element(By.LINK_TEXT, "Back to Home")
            element.click()
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")
# By Partial link text
@pytest.mark.usefixtures("setup")
class TestLocatorByPartialLinkText:
    def test_locator_by_partial_link_text(self):
        try:
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Back to")
            element.click()
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")
# By Xpath
@pytest.mark.usefixtures("setup")
class TestLocatorByXPath:
    def test_locator_by_xpath(self):
        try:
            element = self.driver.find_element(By.XPATH, "//input[@name='last-name']")
            element.send_keys("Mahmuda")
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")
# By Css Selector
@pytest.mark.usefixtures("setup")
class TestLocatorByCssSelector:
    def test_locator_by_css_selector(self):
        try:
            mobile = self.driver.find_element(By.CSS_SELECTOR, "#mobile")
            mobile.send_keys("1886644261")
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")










