import os
import time
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.common.by import By

dotenv_path = find_dotenv()  # finds the .env file path
load_dotenv(dotenv_path)  # loads the .env file from the path found above

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


def sign_in(driver):
    si_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")  # Finds the sign-in button
    si_button.click()
    time.sleep(2)  # Wait 2 seconds for the page to load

    # Fill out the username and password textboxes
    un_textbox = driver.find_element(by=By.ID, value="username")  # Gets username textbox
    un_textbox.send_keys(EMAIL)
    pw_textbox = driver.find_element(by=By.ID, value="password")  # Gets the password textbox
    pw_textbox.send_keys(PASSWORD)

    # Gets the new sign-in button and clicks it
    si_button = driver.find_element(by=By.XPATH,
                                    value='//*[@id="organic-div"]/form/div[3]/button')  # Finds the sign-in button
    si_button.click()
    time.sleep(2)  # Waits for the page to load

def get_jobs(driver):
    jobs = driver.find_elements(by=By.CLASS_NAME, value="jobs-search-results__list-item")
    for job in jobs[:4]:
        job.click()
        time.sleep(2)  # Sleep to give the page time to load

        save_button = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
        save_button.click()