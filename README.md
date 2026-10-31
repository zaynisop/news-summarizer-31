# Lab Assignment 4 – Selenium News Summarizer (Roll No. 31)

- **Registration:** FA23-BCT-031
- **News source:** 31 % 20 + 1 = **12 → Euronews**
- **Selenium language:** Python (Selenium 4 + headless Google Chrome + ChromeDriver)
- **API:** `GET /get?keyword=<keyword>` on port **7000** (starts automatically with the container)

## How it works
1. `scraper.py` opens headless Chrome with Selenium, loads the site's search page
   (`euronews.com/search?query=<keyword>`) and picks the first search result.
2. It opens that article and collects the paragraph text.
3. `summarizer.py` builds an extractive summary (top-scoring sentences by word frequency).
4. `app.py` (Flask, served by gunicorn) returns:
   ```json
   {"registration": "...", "newssource": "...", "keyword": "...", "url": "...", "summary": "..."}
   ```
   The home page `/` shows the registration number.

## Docker Hub image
`zaynop/news-summarizer-31:latest`

```bash
docker pull zaynop/news-summarizer-31:latest
docker run -d -p 7000:7000 zaynop/news-summarizer-31:latest
curl "http://localhost:7000/get?keyword=football"
```

## Build and push yourself
```bash
docker build -t zaynop/news-summarizer-31:latest .
docker push zaynop/news-summarizer-31:latest
```
To use a different registration number without rebuilding: `docker run -e REGISTRATION=FA23-BCT-031 ...`
