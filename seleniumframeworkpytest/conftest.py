import pytest
from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",          # Option name
        action="store",            # Store the option's value
        default="chrome",          # Default value if not provided
    )


@pytest.fixture(scope="class")
def setup(request):
    # # Setup Chrome options
    # options = Options()
    # options.add_experimental_option("detach", True)  # Keeps the browser open after script finishes

    browser_name = request.config.getoption("browser_name").lower()
    if browser_name == "chrome":
        # Setup Chrome options
        # Keeps the browser open after script finishes
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        # Initialize a Chrome browser instance
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        # Setup Firefox options
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        # Setup Edge options
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)

    else:
        # if value is not of chrome,firefox and edge in cmd.
        raise ValueError(f"Browser '{browser_name}' is not supported. Please choose 'chrome', 'firefox', or 'edge'.")

    # Open the webpage
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    # assigning class attribute(class Framework) driver to driver variable present here.
    request.cls.driver = driver
    yield
    driver.close()

