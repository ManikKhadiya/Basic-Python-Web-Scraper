from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time

# List of job sites and their configurations
job_sites = [
    {
        "url": "https://realpython.github.io/fake-jobs/",
        "job_class": ["title", "job-title"],  # List of possible job title classes
        "load_more_class": ["load-more-btn"],  # Possible Load More buttons
        "next_page_text": ["Next", "Next Page"],  # Different Next page buttons
        "uses_infinite_scroll": False,  # Set to True if the site uses infinite scrolling
    },
    # Add more job sites here
]

def scrape_jobs(site):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get(site["url"])
    driver.implicitly_wait(5)

    # Extract job titles
    all_jobs = []

    # 1️⃣ **Handle "Load More" button**
    for button_class in site["load_more_class"]:
        try:
            while True:
                load_more_button = driver.find_element(By.CLASS_NAME, button_class)
                load_more_button.click()
                time.sleep(2)
        except:
            print(f"No more 'Load More' button ({button_class}) found.")

    # 2️⃣ **Handle Infinite Scrolling**
    if site["uses_infinite_scroll"]:
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break  # No more new jobs are loading
            last_height = new_height

    # 3️⃣ **Handle Pagination**
    while True:
        # Extract job titles from the current page
        for job_class in site["job_class"]:
            try:
                job_titles = driver.find_elements(By.CLASS_NAME, job_class)
                for job in job_titles:
                    all_jobs.append(job.text.strip())
            except:
                continue  # Try next class if one fails

        # Find and click "Next Page" button
        next_page_found = False
        for next_button_text in site["next_page_text"]:
            try:
                next_button = driver.find_element(By.LINK_TEXT, next_button_text)
                next_button.click()
                time.sleep(3)
                next_page_found = True
                break  # Stop checking other buttons if one is found
            except:
                continue  # Try next possible button text

        if not next_page_found:
            print("No more pages.")
            break  # Stop if there's no Next button

    driver.quit()
    
    # Print all jobs found
    print(f"Extracted {len(all_jobs)} jobs from {site['url']}")
    for job in all_jobs:
        print(job)

# 🔥 Loop through multiple job sites
for site in job_sites:
    scrape_jobs(site)
# The code above is a template for scraping job sites. It's designed to handle different scenarios like "Load More" buttons, infinite scrolling, and pagination. You can add more job sites to the job_sites list and configure their settings accordingly. The scrape_jobs function will handle the scraping process based on the site's configuration.