from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL=os.getenv("YAHOO_EMAIL")
MY_PASSWORD=os.getenv("YAHOO_PASSWORD")

url="https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0",
"Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",

}
r=requests.get(url,headers=headers)
r.raise_for_status()

soup=BeautifulSoup(r.text,"html.parser")

price=float(soup.find(name="span",class_="a-offscreen").text.strip("INR").replace(",",""))

if price<15000:
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com",port=465) as connection:
                        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
                        connection.sendmail(from_addr=MY_EMAIL,
                                            to_addrs="aadityaaajoshiii@gmail.com",
                                            msg=f"From:{MY_EMAIL}\n"
                f"To:aadityaaajoshiii@gmail.com\n"
                "Subject: Low Price Alert on Amazon!!\n\n"
                f"{soup.find(name="span",class_="a-size-medium product-title-word-break",id="productTitle").text.strip(" ")} is now ${price}\n{url}")
                        print("Message sent successfully")
