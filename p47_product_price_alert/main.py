import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = "https://www.amazon.in/realme-Sunrise-Prolight-Dimensity-SUPERVOOC/dp/B0C78F8RM2/ref=sr_1_2?crid=1KK1WL19NNA7C&dib=eyJ2IjoiMSJ9.poBY6cmbF8qj_QmEuvBsssdGvH7NXiDO5QCEX_FVtvyXGBE5v9alI-nlUWubPHVjbWdeppawnT4nuvqceJpxgQEcWQBG3vdPuv5b2Q38oRAwzY1W0leqFmsCPZ7gHrxPpLycA5B0-ub7TAGesOuBWtCiY2uQ04_WFNGLyeIhPWtcAxEROr-OOcnyxjEr39XqfOKMYYFsqB9ox4xMg8Ym283ftoOGig74TnEbguGZ5B8.JzurOEoYZdHppqRsqeeuPuYHS1ZjTDJyzBOoYDUVTB0&dib_tag=se&keywords=realme%2B11%2Bpro%2B5g&qid=1716191759&sprefix=realme%2B11%2Caps%2C424&sr=8-2&th=1"
MY_EMAIL = "dchirag5050@gmail.com"
APP_PASSWORD = "uldahsssgfnsptkw"

TRIGGER_PRICE = 25000

headers = {
    "User-Agent": "Defined"
}

product_page = requests.get(url=PRODUCT_URL, headers=headers)
soup = BeautifulSoup(markup=product_page.text, features="html.parser")
price_text = soup.find(name="span", class_="a-price-whole").text
price = int(price_text[:-1].replace(",", ""))

if price < TRIGGER_PRICE:
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="dchirag159@gmail.com",
                            msg=f"Subject:Price drop triggered\n\n"
                                f"Price oof realme 11 pro is now {price} "
                                f"below trigger price of {TRIGGER_PRICE}.\n"
                                f"Right time to buy.")
