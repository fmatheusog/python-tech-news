# Requisito 6
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    response = list()

    data = search_news({"title": {"$regex": title, "$options": "1"}})

    for item in data:
        response.append((item["title"], item["url"]))

    return response


# Requisito 7
def search_by_date(date):
    try:
        string_to_date = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = datetime.strftime(string_to_date, "%d/%m/%Y")

        response = list()

        data = search_news({"timestamp": formatted_date})

        for item in data:
            response.append((item["title"], item["url"]))

        return response
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    response = list()

    data = search_news({"tags": {"$regex": tag, "$options": "i"}})

    for item in data:
        response.append((item["title"], item["url"]))

    return response


# Requisito 9
def search_by_category(category):
    response = list()

    data = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    for item in data:
        response.append((item["title"], item["url"]))

    return response
