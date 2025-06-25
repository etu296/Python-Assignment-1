import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

SUPPORTED_BROWSERS = {"chrome", "firefox", "edge"}
DEFAULT_BROWSER = "chrome"
URL = "https://testing-and-learning-hub.vercel.app/index.html"
HEADLESS = True

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

def get_webdriver(browser, headless=HEADLESS):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        if headless:
            options.add_argument("--headless")
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
    return None


@pytest.mark.usefixtures("setup")
class TestHeadlessMode:
    def __init__(self):
        self.driver = None

    def test_headless_mode(self):
        try:
            time.sleep(2)
            print(f"Current URL: {self.driver.current_url}")
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")