import ssl

from bs4 import BeautifulSoup
import requests
import smtplib
# import ssl
smtp_port = 587
smtp_server = "smtp.gmail.com"

# simple_email_context = ssl.create_default_context()
email_from = "YOUEMAIL ID"
email_to = "YOUREMAIL ID
pswd = "YOU PASSWORD " # GENERATED APP PASSWORD BY GOOGLE TRUN ON


#MasterChef 13-in-1 Pressure Cooker- 6 QT Electric Digital Instant MultiPot =
PRODUCT_LINK = "https://www.amazon.com/dp/B079LY61FP/ref=syn_sd_onsite_desktop_58?ie=UTF8&psc=1&pd_rd_plhdr=t"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}
response = requests.get(PRODUCT_LINK, headers=header)
print(response.encoding)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find("span", class_="a-price a-text-price a-size-medium apexPriceToPay").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
print(price)

title = soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE = 70

if price_as_float >= BUY_PRICE:
    message = f"{title} is now ${price_as_float}"

    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(email_from, pswd)
        connection.sendmail(from_addr=email_from, to_addrs=email_to,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_LINK}")
        print("lo")
        connection.close()
