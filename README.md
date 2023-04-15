# Microsoft Careers Web Scraper

Author: Pranav Palagummi, Sid Mangamuri, Anit Annadi, Srish Nigam 
Contributors: Pranav Palagummi, Sid Mangamuri, Anit Annadi, Srish Nigam 

## Description

This is a Python-based web scraping project that extracts job information from the Microsoft careers website (https://careers.microsoft.com/us/en/search-results). The project uses Beautiful Soup and Selenium libraries for web parsing and automation, respectively, to extract job titles, locations, and descriptions from the website.

## Dependencies

The project requires the following dependencies to be installed:

- Python (version 3.8+)
- Beautiful Soup (version 4.9.3)
- Selenium (version 3.141.0)
- ChromeDriver (version 91.0.4472.101)

The project is compatible with Python 3.8+ and has been tested on Windows/Mac/Linux platforms.

## Installation

1. Clone the repository from GitHub: `git clone https://github.com/your-username/microsoft-careers-web-scraper.git`
2. Install the dependencies using pip: `pip install beautifulsoup4==4.9.3 selenium==3.141.0`
3. Download and install the ChromeDriver for your specific OS and version of Chrome from the official ChromeDriver website (https://sites.google.com/a/chromium.org/chromedriver/downloads).
4. Update the `webdriver.Chrome()` function call in the code with the path to the downloaded ChromeDriver executable.

## Usage

1. Run the `microsoft_careers_web_scraper.py` file using a Python interpreter.
2. The program will automatically launch a Chrome browser, navigate to the Microsoft careers website, and extract job information.
3. The extracted job details (title, location, and description) will be displayed on the console.
4. You can modify the code to further process the extracted data, such as saving it to a CSV file or storing it in a database.

## Revision History

- Version 1.0.0: Initial release. [Git commit comment: Add web scraping code]
- Version 1.0.1: Update README file. [Git commit comment: Update README with installation instructions]
- Version 1.0.2: Add error handling. [Git commit comment: Add error handling for page load]
- Version 1.1.0: Refactor code for better performance. [Git commit comment: Refactor code for improved performance]

## License

This project is licensed under the [License Name] license. See the LICENSE file for more details.

