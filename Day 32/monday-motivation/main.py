import smtplib
import datetime as dt
import random

my_email = ""  # Add in your email
pw = ""        # Add in your password

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt", "r") as data_file:
    quotes = data_file.readlines()


if weekday == 0:
    quote_of_day = random.choice(quotes)
    print(quote_of_day)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: It's monday my dudes\n\n{quote_of_day}")
