from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


class WebScraper:
    def __init__(self, website_url, element_class, pagination_xpath, initial_button_index=2, delay_between_requests=3):
        print("Initializing the browser...")
        self.website_url = website_url
        self.element_class = element_class
        self.pagination_xpath = pagination_xpath
        self.initial_button_index = initial_button_index
        self.delay_between_requests = delay_between_requests
        self.driver = self.initialize_driver()
        print("Browser Intitialized\n")
        

    def initialize_driver(self):
        # Set up the Chrome webdriver using ChromeDriverManager
        print("Configuring the browser...")
        #options = webdriver.ChromeOptions()
        #options.add_argument('--ignore-certificate-errors')
        #options.add_argument('--incognito')
        #options.add_argument('--headless')  # Run in headless mode (without opening browser window)
        chromedriver_path = ChromeDriverManager().install() 
        # Start a Selenium webdriver
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service)
        print("Done.")
        return driver

    def scrape_data(self):
        self.driver.get(self.website_url)
        all_data = []
        button_index = self.initial_button_index

        while True:
            # Get the page source after JavaScript execution
            page_source = self.driver.page_source
            
            # Use BeautifulSoup to parse the page source
            soup = BeautifulSoup(page_source, 'html.parser')
            table = soup.find_all('table')[3]  # Replace with your table ID
            
            rows = table.find_all("tr")
            for element in rows:
                all_data.append(element.text)
                print(element.text)  # Replace this with how you want to handle each entry
            
            # Look for the next page link and click it
            try:
                xpath = f'{self.pagination_xpath}[{button_index}]'
                next_page_link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                next_page_link.click()
                button_index += 1
                time.sleep(self.delay_between_requests)  # Add a small delay to ensure the next page content loads (adjust if needed)
            except Exception as e:
                print(f"No more next page link or element found: {e}")
                break

        # Once finished, process 'all_data' as needed (e.g., convert to a DataFrame)
        # df = pd.DataFrame(all_data)
        # print(df)

    def close_driver(self):
        self.driver.quit()
        print("Scrapped")


