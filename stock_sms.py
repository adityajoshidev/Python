import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY=""
NEWS_API_KEY=""
TWILIO_SID=""
TWILIO_AUTH_TOKEN=""
TWILIO_PHONE_NUMBER=""


# STEP 1: Use https://www.alphavantage.co
stock_url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}"
r=requests.get(stock_url)
r.raise_for_status()
data=r.json()["Time Series (Daily)"]

stock_dates=list(data.keys())

yesterday=stock_dates[0]
day_before_yesterday=stock_dates[1]

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
yesterday_close=float(data[yesterday]["4. close"])
day_before_yesterday_close=float(data[day_before_yesterday]["4. close"])
percent_inc_or_dec_in_close=(yesterday_close-day_before_yesterday_close)/day_before_yesterday_close*100
if percent_inc_or_dec_in_close>0:
    inc_or_dec="🔺"
else:
    inc_or_dec="🔻"
if -5>=percent_inc_or_dec_in_close>=5:
    news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"

    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    r = requests.get(news_url)
    r.raise_for_status()
    data = r.json()['articles'][0:3]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for news in data:
        message = client.messages.create(
            body=f"""{int(STOCK)}: {inc_or_dec}{percent_inc_or_dec_in_close}%
    News: {news['title']}""",
            from_=TWILIO_PHONE_NUMBER,
            to="",
        )
## STEP 2: Use https://newsapi.org



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

