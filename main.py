import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_PASSWORD")

PRODUCT_URL = "https://www.amazon.com/Pagal-Basti-Nepali-Saru-Bhakta/dp/1986711366/ref=sr_1_4?crid=35F5CGIXU36KW&keywords=ijoriya+nepali+novel&qid=1668087644&sprefix=ijoriya%2Caps%2C601&sr=8-4"

response = requests.get(PRODUCT_URL, headers={
                        "User-Agent": "Defined", "Accept-Language": "en;q=0.8"})
product_webpage = response.text
# print(product_webpage)

soup = BeautifulSoup(product_webpage, "html.parser")

price = float(soup.find(
    class_="a-size-base a-color-price a-color-price").getText().strip(" $"))
book = soup.find(id="productTitle").getText()
print(type(price))

if price < 23.00:
    print("Price dropped!")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=os.getenv("USER_EMAIL"),
                            msg=f"Subject: Amazon Price Alert!\n\nHey Manish, {book} you are looking for price had dropped below i.e${price}. Purchase it right now!")
