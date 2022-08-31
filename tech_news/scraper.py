from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        for _ in range(10):
            headers = {"user-agent": "Fake user-agent"}
            response = requests.get(url, timeout=3, headers=headers)

            time.sleep(1)

        if (response.status_code != 200):
            return None

        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get()
    date = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    summary = selector.css(".entry-content > p:nth-of-type(1) ::text").getall()
    comments = selector.css(".post-comments .title-block::text").getall()
    tags = selector.css(".post-tags li a::text").getall()
    category = selector.css(".meta-category .label::text").get()

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": date,
        "writer": writer,
        "comments_count": len(comments),
        "summary": "".join(summary).strip(),
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
