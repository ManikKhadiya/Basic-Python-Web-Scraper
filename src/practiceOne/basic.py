import requests
from bs4 import BeautifulSoup

# fake jobs website
url = "https://realpython.github.io/fake-jobs/"

# Get contents
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract job titles
jobs = soup.find_all("h2", class_="title is-5")
for job in jobs:
    print(job.text.strip())  # Print job title
