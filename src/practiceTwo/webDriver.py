from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# set up firefox webdriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# opens url
url = "https://realpython.github.io/fake-jobs/"
driver.get(url)

# wait for page to load
driver.implicitly_wait(5)  # for 5 sec

# extract titeles
job_titles = driver.find_elements(By.CLASS_NAME, "title")

# porint titels
for job in job_titles:
    print(job.text.strip())

# clsoes browser
driver.quit()
