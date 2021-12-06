# -*- coding:utf-8 -*-
from requests import get
from bs4 import BeautifulSoup


def category():
    
    url = "https://www.football.fr/espagne"

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
    }
    response = get(url, headers=headers)
    html_soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 200:

        # main_div = html_soup.find("div", attrs={"class": "archive-posts row"})
        
        nav_category = html_soup.find("div", attrs={"id": "principal-menu"})
        li_category = nav_category.find_all("li")
        list_cat = ["https://www.football.fr/les-tops"]
        for element in li_category:
            link_cat = element.find('a')['href']
            title_cat = element.text.strip()
            list_cat.append(link_cat)
            # list_cat = [link_cat, title_cat]
        # print(list_cat)
        return list_cat
        
    
    else:
        print("erreur statut", response.status_code)


def link_actu(url):
    
    # url = "https://www.football.fr/espagne"

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
    }
    response = get(url, headers=headers)
    html_soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 200:

        # main_div = html_soup.find("div", attrs={"class": "archive-posts row"})
        
        nav_link = html_soup.find_all("a", attrs={"class": "page-numbers"})[7].text.strip()
        all_links = []
        for item in range(1,int(nav_link)+1):
            url2 = f"{url}/page/{item}"
            # print(url2)
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
            }
            response = get(url2, headers=headers)
            html_soup = BeautifulSoup(response.text, "html.parser")
            
            div_link = html_soup.find_all("div", attrs={"class": "post-item-img"})
            list_link = [element.find("div")["data-href"] for element in div_link]
            all_links.append(list_link)
        # print(all_links)
        return all_links
        
    
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
        try:
            short_desc = (
                html_soup.find("div", attrs={"class": "post-excerpt"})
                .text.strip()
                .replace("\xa0", " ")
                .replace("\n", "")
            )
        except:
            short_desc = ""
            print("Pas de short desc")
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

categories_links = category()
for elt in categories_links:
    links = link_actu(elt)
    for item in links:
        for link in item:
            actu(link)
