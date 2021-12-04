# -*- coding:utf-8 -*-
from requests import get
from bs4 import BeautifulSoup


def link_actu():
    
    url = "https://www.football.fr/les-tops"

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
    }
    response = get(url, headers=headers)
    html_soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 200:

        # main_div = html_soup.find("div", attrs={"class": "archive-posts row"})
        div_link = html_soup.find_all("div", attrs={"class": "post-item-img"})
        list_link = [element.find("div")["data-href"] for element in div_link]
        return list_link
    else:
        print("erreur statut", response.status_code)


def actu(link):

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
    }
    response = get(link, headers=headers)
    html_soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 200:

        # actu_article = html_soup.find("article")
        autor_and_date = (
            html_soup.find("div", attrs={"class": "post-info"})
            .text.strip()
            .replace("\xa0", " ")
            .replace("\n", "")
        )
        title = html_soup.find("h1", attrs={"class": "post-title"}).text
        image = html_soup.find("img")["src"]
        short_desc = (
            html_soup.find("div", attrs={"class": "post-excerpt"})
            .text.strip()
            .replace("\xa0", " ")
            .replace("\n", "")
        )
        description = (
            html_soup.find("div", attrs={"class": "post-content"})
            .text.strip()
            .replace("\xa0", " ")
            .replace("\n", "")
        )
        article = {
            "author": autor_and_date,
            "title": title,
            "image": image,
            "short_desc": short_desc,
            "description": description,
        }
        print(article)
        return article
        # print("ok actu", div_link.text)
    else:
        print("erreur statut", response.status_code)


links = link_actu()
for link in links:
    actu(link)
