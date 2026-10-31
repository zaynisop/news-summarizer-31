import os

# Roll No. 31 -> 31 % 20 + 1 = 12 -> Euronews
REGISTRATION = os.getenv("REGISTRATION", "FA23-BCT-031")
NEWS_SOURCE = "Euronews"
NEWS_DOMAIN = "euronews.com"
SEARCH_URL = "https://www.euronews.com/search?query={q}"
# Links inside the search-result list (not the "most viewed" sidebar or nav menus)
RESULT_SELECTOR = ".b-listing__main article a.the-media-object__link"
# Article URLs look like /2026/10/30/some-slug or /my-europe/2026/10/30/some-slug
ARTICLE_PATTERN = r"euronews\.com/(?:[a-z-]+/)*\d{4}/\d{2}/\d{2}/[a-z0-9-]+"
