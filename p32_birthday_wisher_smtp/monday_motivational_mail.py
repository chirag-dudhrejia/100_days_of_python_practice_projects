import smtplib
import datetime as dt
import random

MY_EMAIL = "dchirag5050@gmail.com"
APP_PASSWORD = "uldahsssgfnsptkw"

now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt", "r", encoding="utf8") as read_quote:
        quotes = read_quote.readlines()

    selected_quote = str(random.choice(quotes)).replace('”–', " - ").encode('ascii', 'ignore')
    print(selected_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="dchirag159@gmail.com",
                            msg=f"Subject:Motivation lelo\n\n{selected_quote.decode('utf-8', "ignore")}")