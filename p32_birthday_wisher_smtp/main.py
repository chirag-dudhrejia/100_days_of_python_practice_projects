import smtplib
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "dchirag5050@gmail.com"
password = "uldahsssgfnsptkw"
letters = ["letter1.txt", "letter2.txt", "letter3.txt"]

now = dt.datetime.now()

birthdays = pd.read_csv("birthdays.csv")
today_birthday = birthdays[(birthdays["month"] == now.month) & (birthdays["day"] == now.day)]
if len(today_birthday) > 0:
    for row in today_birthday.values:
        name = row[0]
        email = row[1]

        letter = random.choice(letters)
        with open(file=f"letters/{letter}", mode="r") as letter_format:
            letter_text = letter_format.read()
            letter_text = letter_text.replace("[Name]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="dchirag159@gmail.com",
                                msg=f"Subject: Birthday Wish\n\n{letter_text}")