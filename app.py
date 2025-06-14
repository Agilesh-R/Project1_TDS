from fastapi import FastAPI
from discourse_downloader_single import run_scraper_programmatically

app = FastAPI()

@app.get("/")
def root():
    return {"message": "TDS Scraper API is live."}

@app.post("/scrape")
def scrape():
    try:
        run_scraper_programmatically()
        return {"status": "success", "message": "Scraping completed."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
