import pandas as pd
import datetime as dt
import random
import smtplib

my_email = ""  # Add in your email
pw = ""        # Add in your password

people = pd.read_csv("birthdays.csv")  # Add your own friends and families in there
birthdays_dict = people.to_dict(orient="records")


now = dt.datetime.now()
month_day = now.day
month = now.month

for person in birthdays_dict:
    if person["day"] == month_day and person["month"] == month:
        random_letter_index = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_letter_index}.txt") as template:
            letter = template.read()
        complete_letter = letter.replace("[NAME]", person["name"])
        print(complete_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=pw)
            connection.sendmail(from_addr=my_email, to_addrs=person["email"],
                                msg=f"Subject: Happy Birthday!\n\n{complete_letter}")
