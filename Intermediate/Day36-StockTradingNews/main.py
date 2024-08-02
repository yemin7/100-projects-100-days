import requests
from format_date import FormatDate
from send_sms import SendSMS

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ACCOUNT_SID = ''
AUTH_TOKEN = ''
SENDER_PHONE = ''
RECEIVER_PHONE = ''

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

alpha_apikey = ""
newsapi_apikey = ""
FORMAT_DATE_STRING = "%Y%m%dT%H%M"
FORMAT_DATE_STRING2 = "%Y-%m-%d"
format_time = FormatDate()

alphavantage_url = "https://www.alphavantage.co/query"
newsapi_url = "https://newsapi.org/v2/everything"

# news_sentiment_parameters = {
#     "function": "NEWS_SENTIMENT",
#     "tickers": STOCK,
#     "apikey": alpha_apikey,
#     "time_from": format_time.format_yesterday(FORMAT_DATE_STRING),
#     "time_to": format_time.format_before_yesterday(FORMAT_DATE_STRING),
# }

alphavantage_time_series_daily_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_apikey,
}


def get_data(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()
    else:
        return None


def calculate_percentage(yest_data, b_yest_data):
    difference = yest_data - b_yest_data
    if difference > 0:
        price = "🔺"
    else:
        price = "🔻"
    diff_percent = round((difference / yest_data) * 100)
    return diff_percent, price


news_data = get_data(alphavantage_url, alphavantage_time_series_daily_parameters)['Time Series (Daily)']
yesterday = format_time.format_yesterday(FORMAT_DATE_STRING2)
before_yesterday = format_time.format_before_yesterday(FORMAT_DATE_STRING2)
closing_price_yesterday = float(news_data[yesterday]['4. close'])
closing_price_before_yesterday = float(news_data[before_yesterday]['4. close'])

# print(f"Yesterday data: {news_data[yesterday]}")
# print(f"Before Yesterday data: {news_data[before_yesterday]}")

percentage, up_down = calculate_percentage(closing_price_yesterday, closing_price_before_yesterday)
# print(f"Percentage: {percentage}")
# print(f"Increase or Decrease: {up_down}")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(percentage) > 1:
    news_param_with_date = {
        "q": COMPANY_NAME.lower(),
        "from": yesterday,
        "to": before_yesterday,
        "sortBy": "popularity",
        "language": "en",
        "apiKey": newsapi_apikey
    }

    news_article = get_data(url=newsapi_url, params=news_param_with_date)
    three_articles = news_article["articles"][:3]
    articles_info = [f"Headline: {articles['title']}.\nBrief: {articles['description']}" for articles in three_articles]

    send_message = SendSMS(ACCOUNT_SID, AUTH_TOKEN, SENDER_PHONE, RECEIVER_PHONE)
    for i in articles_info:
        message = f"{STOCK}: {up_down}{abs(percentage)}%\n{i}"
        send_message.send(message)
