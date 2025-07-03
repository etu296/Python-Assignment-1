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
class TestLocatorByContains:
    def test_locator_by_contains(self):
        try:
            # contain Xpath
            contains = self.driver.find_element(By.XPATH,"//*[contains(@placeholder , 'Enter your first name')]")
            contains.send_keys("Etu")
            time.sleep(3)
            # By ARIA Attributes
            aria = self.driver.find_element(By.XPATH,"//*[@aria-label='New York']")
            aria.click()
            time.sleep(3)
            #By And Expression
            and_expression = self.driver.find_element(By.XPATH,"//input[@name = 'last-name' and @placeholder = 'Enter your last name']")
            and_expression.send_keys("Mahmuda")
            time.sleep(2)
            # By And Expression
            element = self.driver.find_element(By.XPATH,"//input[@id='qualification' or @name='qualification' or @placeholder='Enter your qualification']")
            element.send_keys("SQA")
            time.sleep(5)

        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")