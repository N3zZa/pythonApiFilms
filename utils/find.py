import requests
from bs4 import BeautifulSoup


def main(search_query):
    url = f"https://hdrezka.ag/index.php?do=search&subaction=search&story={search_query}&search_start=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find_all("div", class_="b-content__inline_item")
    if not search_results:
        print("По вашему запросу ничего не найдено.")
    else:
        for result in search_results:
            link = result.find("a")["href"]
            title = result.find("a")["title"]
            print(f"{title}: {link}")




