import requests
from bs4 import BeautifulSoup
import csv
import os

class BookScraper:
    """Handles the extraction of book data from Books to Scrape."""
    
    def __init__(self, base_url, output_dir="scraped_data"):
        self.base_url = base_url
        self.output_dir = output_dir
        self.categories = []
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _get_soup(self, url):
        """Internal helper to fetch soup."""
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return BeautifulSoup(r.content, "html.parser")
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            return None

    def fetch_categories(self):
        """Finds all category links from the sidebar."""
        soup = self._get_soup(self.base_url)
        if not soup: return
        
        links = soup.find("div", class_="side_categories").find_all("a")
        for a in links[1:]: ## we skippping 'Books' general category ##
            self.categories.append({
                "name": a.text.strip(),
                "url": self.base_url + a["href"]
            })

    def scrape_all(self):
        """Loop through categories and save CSVs."""
        self.fetch_categories()
        for cat in self.categories:
            print(f"Scraping {cat['name']}...")
            self._save_category_to_csv(cat)

    def _save_category_to_csv(self, category):
        """Scrapes books and writes to file."""
        soup = self._get_soup(category["url"])
        if not soup: return

        cards = soup.find_all("article", class_="product_pod")
        file_path = os.path.join(self.output_dir, f"{category['name']}.csv")

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Price", "Availability"])
            for card in cards:
                writer.writerow([
                    card.h3.a["title"],
                    card.find("p", class_="price_color").text,
                    card.find("p", class_="instock availability").text.strip()
                ])
                
        print(f"Saved data to {file_path}")
        
        
        