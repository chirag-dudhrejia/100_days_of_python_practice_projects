from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")


def get_money():
    money = driver.find_element(By.ID, value="money")
    return int(money.text.replace(",", ""))


def get_cursor():
    buy_cursor = driver.find_element(By.ID, value="buyCursor")
    return buy_cursor


def get_grandma():
    buy_grandma = driver.find_element(By.ID, value="buyGrandma")
    return buy_grandma


def get_factory():
    buy_factory = driver.find_element(By.ID, value="buyFactory")
    return buy_factory


def get_mine():
    buy_mine = driver.find_element(By.ID, value="buyMine")
    return buy_mine


def get_shipment():
    buy_shipment = driver.find_element(By.ID, value="buyShipment")
    return buy_shipment


def get_alchemy():
    buy_alchemy = driver.find_element(By.ID, value="buyAlchemy lab")
    return buy_alchemy


def get_portal():
    buy_portal = driver.find_element(By.ID, value="buyPortal")
    return buy_portal


def get_time_machine():
    buy_time_machine = driver.find_element(By.ID, value="buyTime machine")
    return buy_time_machine


def click_per_second():
    text = driver.find_element(By.ID, value="cps")
    return float(text.text.split(" : ")[1].replace(",", ""))


def get_amount(item_id):
    item = driver.find_element(By.ID, value=item_id)
    amount_tag = item.find_element(By.TAG_NAME, value="b")
    amount = int(amount_tag.text.split(" - ")[1].replace(",", ""))
    return amount


end_time = time.time() + (60 * 5)
timestamp = time.time() + 5
while end_time > time.time():
    cookie.click()
    if timestamp <= time.time():
        timestamp += 5
        if get_money() > get_amount("buyTime machine"):
            get_time_machine().click()
        elif get_money() > get_amount("buyPortal"):
            get_portal().click()
        elif get_money() > get_amount("buyAlchemy lab"):
            get_alchemy().click()
        elif get_money() > get_amount("buyShipment"):
            get_shipment().click()
        elif get_money() > get_amount("buyMine"):
            get_mine().click()
        elif get_money() > get_amount("buyFactory"):
            get_factory().click()
        elif get_money() > get_amount("buyGrandma"):
            get_grandma().click()
        elif get_money() > get_amount("buyCursor"):
            get_cursor().click()

print(click_per_second())