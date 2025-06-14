from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from discourse_downloader_single import run_scraper_programmatically

app = FastAPI()

# ✅ Allow all CORS origins (or restrict to exam site if known)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or set to specific domain like ["https://exam.iitm.ac.in"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "TDS Scraper API is live."}

@app.post("/scrape")
def scrape():
    try:
        run_scraper_programmatically()
        return {"status": "success", "message": "Scraping completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
