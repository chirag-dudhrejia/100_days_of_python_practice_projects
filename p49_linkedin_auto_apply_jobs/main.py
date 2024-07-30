from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.linkedin.com/home")

driver.find_element(By.CLASS_NAME, value="nav__button-secondary").click()

username_field = driver.find_element(By.ID, value="username")
username_field.send_keys("dchirag159@gmail.com")
password_field = driver.find_element(By.ID, value="password")
password_field.send_keys("chirag159")

driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button").click()