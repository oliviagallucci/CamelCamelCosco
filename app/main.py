from fastapi import FastAPI, Query
from scraper import scrape_costco
from typing import List

app = FastAPI()

@app.get("/api/scrape")
def search_products(q: str = Query(..., description="Search query for Costco")):
    try:
        results = scrape_costco(q)
        return {"query": q, "results": results}
    except Exception as e:
        return {"error": str(e)}

