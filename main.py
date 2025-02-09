import requests
import datetime

# ScraperAPI setup
SCRAPER_API_KEY = "66344a1ee064477d87b4d160c4283648"
GOLD_PRICE_URL = f"http://api.scraperapi.com?api_key={SCRAPER_API_KEY}&url=https://www.goodreturns.in/gold-rates/"

# Fetch gold price
def fetch_gold_price():
    response = requests.get(GOLD_PRICE_URL)
    if response.status_code == 200:
        html = response.text
        match = html.split("Hyderabad")[1].split("₹")[1].split("<")[0] if "Hyderabad" in html else None
        return f"22K Gold Price in Hyderabad: ₹{match.strip()}" if match else "Price not found"
    return "Failed to fetch gold price."

# Save result to a file
gold_price = fetch_gold_price()
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
result = f"[{timestamp} IST] {gold_price}\n"

with open("gold_price_log.txt", "a") as file:
    file.write(result)

print(result)
