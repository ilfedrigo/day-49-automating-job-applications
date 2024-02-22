from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = "contato.fedrigo@gmail.com"
password_str = "lakers97"

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3812551330&distance=25&f_AL=true&geoId=106057199&keywords=Desenvolvedor%20Python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

enter_login = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
enter_login.click()

time.sleep(1)

# Finding the login and password elements and entering credentials
login = driver.find_element(By.NAME, "session_key")
password = driver.find_element(By.NAME, "session_password")

login.send_keys(username)
password.send_keys(password_str)
password.send_keys(Keys.RETURN)

# Waiting for a few seconds for the page to load
time.sleep(1)

save_job = driver.find_element(By.CSS_SELECTOR, "button .jobs-save-button")
save_job.click()

time.sleep(1)