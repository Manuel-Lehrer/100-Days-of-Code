import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Create a separate .env file to store your information corresponding to the variable names
api_key = os.getenv('API_KEY')
api_key_news = os.getenv('API_KEY_NEWS')
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
phone_number = os.getenv('PHONE_NUMBER')

# Feel free to change this to the stock/company of your liking
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

change_per = 0
up_down = ""


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "30min",
    "extended_hours": "false",
    "apikey": api_key,
}


def stock_changed():
    global change_per, up_down
    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    stock_data = response.json()["Time Series (Daily)"]

    last_two = []

    for index, (key, value) in enumerate(stock_data.items()):
        if index >= 2:
            break
        last_two.append(value["4. close"])

    today_close = float(last_two[0])

    yesterday_close = float(last_two[1])

    change = today_close-yesterday_close
    if change > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    change_per = change / today_close * 100

    if abs(change_per) > 5:
        return True


def get_news():

    parameters1 = {
             "qInTitle": COMPANY_NAME,
             "apiKey": api_key_news,
    }

    response1 = requests.get("https://newsapi.org/v2/everything", params=parameters1)

    all_articles = response1.json()["articles"]

    not_formatted_articles = all_articles[:3]
    formatted = [f"Headline: {news['title']}. \n Brief: {news['brief']}" for news in not_formatted_articles]

    return formatted


if stock_changed():
    formatted_articles = get_news()
    client = Client(account_sid, auth_token)
    for articles in formatted_articles:
        message = client.messages.create(
            from_=twilio_number,
            body=f"{STOCK} {up_down}%: {change_per}% \n {articles}",
            to=phone_number,
        )
