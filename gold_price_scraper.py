import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import os

# ScraperAPI Key (from GitHub Secrets)
API_KEY = os.getenv("SCRAPER_API_KEY")
URL = f"http://api.scraperapi.com?api_key={API_KEY}&url=https://www.goodreturns.in/gold-rates/"

# Twilio Credentials (from GitHub Secrets)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = "whatsapp:+14155238886"  # Twilio sandbox number
TWILIO_WHATSAPP_TO = os.getenv("TWILIO_WHATSAPP_TO")  # Your WhatsApp number

def fetch_gold_price():
    response = requests.get(URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the table that contains city-wise gold prices
        tables = soup.find_all("table")  
        if len(tables) >= 4:  # Table 4 contains city-wise prices
            rows = tables[3].find_all("tr")  # Get all rows
            
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 3 and "Hyderabad" in cols[0].text:
                    gold_22k = cols[1].text.strip()
                    return gold_22k
        return "City-wise gold price table not found."
    else:
        return f"Failed to fetch data. Status Code: {response.status_code}"

def send_whatsapp_message(price):
    if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN and TWILIO_WHATSAPP_TO:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_FROM,
            body=f"🌟 22K Gold Price in Hyderabad: {price} 🌟",
            to=TWILIO_WHATSAPP_TO
        )
        print(f"WhatsApp message sent: {message.sid}")
    else:
        print("Twilio credentials not set. Skipping WhatsApp message.")

if __name__ == "__main__":
    gold_price = fetch_gold_price()
    print(f"22K Gold Price in Hyderabad: {gold_price}")
    send_whatsapp_message(gold_price)  # Send WhatsApp message
