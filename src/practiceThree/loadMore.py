from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# set up firefox webdriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Open the job site (this is a test site, replace with a real one)
url = "https://realpython.github.io/fake-jobs/"
driver.get(url)

# wait 5 sec for page to load
driver.implicitly_wait(5)

# clicking "Load More" button until it's gone
while True:
    try:
        load_more_button = driver.find_element(By.CLASS_NAME, "load-more-btn")
        load_more_button.click()
        time.sleep(2)  # Wait for new jobs to load
    except:
        print("No more 'Load More' button found.")
        break  # Exit loop if button is missing

# Extract all job titles
job_titles = driver.find_elements(By.CLASS_NAME, "title")
for job in job_titles:
    print(job.text.strip())

# Close browser
driver.quit()
# The code above will keep clicking the "Load More" button until it's gone. This way, you can extract all the job titles from the site.