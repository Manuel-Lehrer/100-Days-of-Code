from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

my_email = os.environ["EMAIL"]
pw = os.environ["PW"]

item_link = "" #Choose the product you want to track

# Scraping Amazons product
response = requests.get(item_link,
                        headers={
                            "Accept-language": "en-US, en;q=0.9",
                            "accept-encoding": "gzip, deflate, br",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                                      "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
                        })


webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
print(soup.prettify())

price = float(soup.find("span", class_="aok-offscreen").getText().split("$")[1])

if price < 90:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: Amazon Price Alert!\n\nThe item is now available for ${price}\n"
                                f"Get it here: {item_link}")
