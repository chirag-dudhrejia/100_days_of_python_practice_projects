from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

articles_count_text = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a").text
articles_count = int(articles_count_text.replace(",", ""))
print(articles_count)

driver.quit()