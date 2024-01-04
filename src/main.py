import config
from scrapper import WebScraper

if __name__ == "__main__":
    example_url = 'https://h1bgrader.com/job-titles/data-scientist-d0g9n44qko#job-h1b-sponsors'
    example_element_class = 'your_element_class'
    example_pagination_xpath = '//*[@id="h1bsponsor-by-job_paginate"]/ul/li'

    # Create a scraper instance
    scraper = WebScraper(example_url, example_element_class, example_pagination_xpath)

    # Start scraping
    scraper.scrape_data()

    # Close the webdriver
    scraper.close_driver()