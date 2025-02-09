import requests
from bs4 import BeautifulSoup

# ScraperAPI Key
API_KEY = "66344a1ee064477d87b4d160c4283648"  # Replace with your real API key
URL = f"http://api.scraperapi.com?api_key={API_KEY}&url=https://www.goodreturns.in/gold-rates/"

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

if __name__ == "__main__":
    gold_price = fetch_gold_price()
    print(f"22K Gold Price in Hyderabad: {gold_price}")
