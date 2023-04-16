import time
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_source(url):
    """
    Fetches the page source of the given URL using Selenium WebDriver.

    Args:
        url (str): The URL to fetch page source from.

    Returns:
        str: The page source of the URL.
    """
    driver = webdriver.Chrome('/path/to/chromedriver') # Initialize Chrome WebDriver
    driver.get(url) # Open the URL in the WebDriver
    time.sleep(3) # Add a delay to allow page to load
    page_source = driver.page_source # Get the page source
    driver.quit() # Close the WebDriver
    return page_source

def parse_job_cards(page_source):
    """
    Parses job cards from the page source using BeautifulSoup.

    Args:
        page_source (str): The page source to parse.

    Returns:
        list: A list of dictionaries containing job details.
    """
    soup = BeautifulSoup(page_source, 'html.parser') # Initialize BeautifulSoup with page source
    job_cards = soup.find_all('li', class_='c-search-result-item') # Find all job cards
    jobs = []
    for card in job_cards:
        job = {}
        job['title'] = card.find('h3', class_='c-job-card-title').text.strip() # Extract job title
        job['location'] = card.find('div', class_='c-job-card-location').text.strip() # Extract job location
        job['description'] = card.find('div', class_='c-job-card-description').text.strip() # Extract job description
        jobs.append(job)
    return jobs

def print_job_details(jobs):
    """
    Prints job details from the list of job dictionaries.

    Args:
        jobs (list): A list of dictionaries containing job details.
    """
    for job in jobs:
        print('Title:', job['title'])
        print('Location:', job['location'])
        print('Description:', job['description'])
        print('---')

# Main program
url = 'https://careers.microsoft.com/us/en/search-results'
page_source = get_page_source(url)
jobs = parse_job_cards(page_source)
print_job_details(jobs)
