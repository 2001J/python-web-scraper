import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("span", class_="text")

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote"])

    for quote in quotes:
        writer.writerow([quote.text])

print("Done. Quotes saved to quotes.csv")
