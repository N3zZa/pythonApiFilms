import requests
from bs4 import BeautifulSoup


def get_link(url):
    # Отправляем запрос на страницу
    response = requests.get(url)
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Получаем список всех iframe на странице
    iframes = soup.find_all('iframe')
    if len(iframes) > 0:
        # Получаем src первого iframe
        iframe_src = iframes[0]['src']

        # Отправляем запрос на страницу с видео
        response = requests.get(iframe_src)

        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Получаем ссылку на видео
        video_src = soup.find('source')['src']

        print(video_src)
    else:
        print("Нет iframe на странице")

