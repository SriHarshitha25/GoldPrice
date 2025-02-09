import requests

def fetch_gold_price():
    url = "https://www.goodreturns.in/gold-rates/hyderabad.html"  
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        if "Hyderabad" in html and "₹" in html:
            try:
                gold_price = html.split("Hyderabad")[1].split("₹")[1].split("<")[0]
                return gold_price
            except IndexError:
                return "Gold price format changed, update script."
        else:
            return "Gold price not found in page."
    else:
        return "Failed to fetch gold price."

if __name__ == "__main__":
    gold_price = fetch_gold_price()
    print("22K Gold Price in Hyderabad:", gold_price)
