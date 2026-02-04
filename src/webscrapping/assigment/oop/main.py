from src.bookScrapper import BookScraper

def main():
    
    
    BASE_URL = "https://books.toscrape.com/"
    OUTPUT_FOLDER = "category_results"


    scrapper = BookScraper(BASE_URL, output_dir=OUTPUT_FOLDER)

    print("--- Starting Scraper ---")
    scrapper.scrape_all()
    print("--- Scraping Complete ---")

if __name__ == "__main__":
    main()