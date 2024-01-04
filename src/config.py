# Configuration parameters for web scraping

# Initial Setup
website_url = "https://h1bgrader.com/job-titles/data-scientist-d0g9n44qko#job-h1b-sponsors"
jobsearch_tab_xpath = '//*[@id="pills-tab"]/li[2]'
search_box_xpath = '//*[@id="pills-job"]/form/div'


#Result Page Setup
company_listingtab_xpath = '//*[@id="employer-tabs"]/li[3]'
table_element_id = 3 # Three table present in find_all search

#Pagination
pagination_xpath = "//*[@id='h1bsponsor-by-job_paginate']/ul/li"
initial_button_index = 2
delay_between_requests = 3
