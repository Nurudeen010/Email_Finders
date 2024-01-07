from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import the Options class
from webdriver_manager.chrome import ChromeDriverManager

def ScrapLink(url):
    # Set up the Chrome WebDriver with Selenium
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode to avoid opening a visible browser window
    driver = webdriver.Chrome(options=options)

    # Navigate to the URL
    driver.get(url)

    # Wait for dynamic content to load (you may need to adjust the wait time)
    driver.implicitly_wait(0.05)

    # Extract the page source after dynamic content has loaded
    page_source = driver.page_source

    # Use BeautifulSoup and regex to find email addresses
    soup = BeautifulSoup(page_source, "html.parser")
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@(facebook\.com|[A-Za-z0-9.-]+\.[A-Za-z]{2,})\b')
    
     # Find HTML elements that may contain email addresses
    email_elements = soup.find_all(['a', 'p', 'span', 'div', 'td'], string=email_pattern)

    # Extract text content from those elements
    emails = [email_pattern.search(element.get_text()).group() for element in email_elements if email_pattern.search(element.get_text())]

    # Close the WebDriver
    driver.quit()

    return emails
