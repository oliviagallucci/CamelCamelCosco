from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime
import os

# TODO research how the urls work 
# search_url = f"https://www.costco.com/s?dept=All&keyword={query.replace(' ', '+')}"
# https://www.costco.com/s?keyword=hello

def get_formatted_datetime():
    now = datetime.now()
    formatted = now.strftime("%m-%d-%Y-%H:%M:%S")
    return formatted

def scrape_costco(query: str):
    search_url = f"https://www.costco.com/s?dept=All&keyword={query.replace(' ', '+')}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(search_url, timeout=60000)
        page.wait_for_selector(".product-tile-set", timeout=15000)

        products = []
        tiles = page.query_selector_all(".product-tile-set")

        for tile in tiles:
            try:
                title = tile.query_selector(".description").inner_text().strip()
                price_el = tile.query_selector(".price")
                price = price_el.inner_text().strip() if price_el else "N/A"
                link = tile.query_selector("a").get_attribute("href")
                full_url = link if link.startswith("http") else f"https://www.costco.com{link}"

                products.append({
                    "title": title,
                    "price": price,
                    "url": full_url
                })
            except Exception:
                continue

        browser.close()

        # create data directory one level up if it does not exist
        output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
        os.makedirs(output_dir, exist_ok=True)

        # save to csv
        df = pd.DataFrame(products)
        formatted_date = get_formatted_datetime()
        filename = f"{formatted_date}-{query.replace(' ', '_')}.csv"
        filepath = os.path.join(output_dir, filename)
        df.to_csv(filepath, index=False)
        print(f"[✓] saved {len(products)} results to {filename}")

        return products
    
    