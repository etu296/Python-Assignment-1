import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.expected_conditions import none_of
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

SUPPORTED_BROWSERS = {"chrome", "firefox", "edge"}
DEFAULT_BROWSER = "chrome"
URL = "https://testing-and-learning-hub.vercel.app/index.html"

def get_webdriver(browser):
    if browser == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        return webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
    elif browser == "edge":
        return webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))
    return None
@pytest.fixture(scope="class")
def setup(request, browser = DEFAULT_BROWSER):
    # Step-1: Browser Support Check
    if browser not in SUPPORTED_BROWSERS:
        raise ValueError(f"Browser '{browser}' is not supported")
    # Step-2: Driver instance get
    driver = get_webdriver(browser)

    # Step-3: Maximize the browser
    driver.maximize_window()

    # Step-4: Open the URL
    driver.get(URL)

    # Step-5:
    request.cls.driver = driver

    # Step-6:
    yield
    driver.quit()
@pytest.mark.usefixtures("setup")
class TestOpenBrowser:
    def test_open_browser(self):
        try:
            username = self.driver.find_element(By.ID, "loginEmail")
            username.send_keys("etu@gmail.com")
            time.sleep(2)
            password = self.driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
            password.send_keys("pass")
            time.sleep(2)
            button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            button.click()
            time.sleep(2)
            print("Browser opened successfully!")
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")