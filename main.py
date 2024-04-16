import time
import index
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager
from selenium.webdriver.chrome.service import Service as ChromeService

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3240956260&f_AL=true&keywords=python%20developer'

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
# Keep the browser open when the script finishes - unless you use driver.quit()

service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url=URL)  # Gets a webpage

time.sleep(2)

index.sign_in(driver)  # Finds the sign-in button then signs the user in
index.get_jobs(driver)  # Gets a list of jobs and saves each one

driver.quit()
