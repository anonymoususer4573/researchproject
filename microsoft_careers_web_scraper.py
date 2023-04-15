import time
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_source(url):
    driver = webdriver.Chrome('/path/to/chromedriver')
    driver.get(url)
    time.sleep(3)
    page_source = driver.page_source
    driver.quit()
    return page_source

def parse_job_cards(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    job_cards = soup.find_all('li', class_='c-search-result-item')
    jobs = []
    for card in job_cards:
        job = {}
        job['title'] = card.find('h3', class_='c-job-card-title').text.strip()
        job['location'] = card.find('div', class_='c-job-card-location').text.strip()
        job['description'] = card.find('div', class_='c-job-card-description').text.strip()
        jobs.append(job)
    return jobs

def print_job_details(jobs):
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
