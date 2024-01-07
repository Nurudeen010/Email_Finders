# Web Scraping and Email Extraction

## Overview
This project is a Python-based web scraping tool for extracting email addresses from a list of specified URLs. It utilizes BeautifulSoup for HTML parsing and Selenium for dynamic content loading.

## Features
- Headless web scraping using Selenium to avoid visible browser window
- Email extraction with BeautifulSoup and regex patterns
- Handling of dynamic content loading for JavaScript-based websites

## Getting Started
### Prerequisites
- Python 3.x
- Dependencies: Beautiful Soup, Selenium, webdriver_manager

### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/web-scraping-email-extraction.git
2. cd web-scraping-email-extraction
3. pip install -r requirements.txt

### Usage
1. Add URLs to the urls list in scrapper.py.
2. Run the script: python scrapper.py
3. Check the generated emails.csv file for extracted email addresses.

### Contribution
1. Adjust the wait time for dynamic content loading in ScrapLink function (driver.implicitly_wait()).
2. Customize the email extraction regex pattern in ScrapLink function (email_pattern).

### Contributing
Contributions are welcome! Fork the repository and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgments
Inspired by the need for a simple and efficient email extraction tool.
Thanks to the developers of BeautifulSoup, Selenium, and webdriver_manager.
