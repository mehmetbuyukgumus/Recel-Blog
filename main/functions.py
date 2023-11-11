import pandas as pd
from bs4 import BeautifulSoup
import requests

#133

links_column = []
title_column = []
article_column = []



def connect_to_page():
    soups = []
    for i in range(1,134):
        url = f"http://recel-blog.com/page/{i}"
        headers = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"}
        page = requests.get(url, headers= headers)
        soups.append(BeautifulSoup(page.content, "lxml"))
    return soups

def get_links(soups):
    for soup in soups:
        title = soup.find_all("h2", attrs = {"class": "entry-title h3"})
        for links in title:
            link = links.find_all("a")
            for a in link:
                link_text = a.get("href")
                links_column.append(link_text)

def get_title(soups):
     for soup in soups:
        title = soup.find_all("h2", attrs = {"class": "entry-title h3"})
        for links in title:
            link = links.find("a")
            title_column.append(link.get_text())
            
def get_article():
    for link in links_column:
        headers = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"}
        page = requests.get(link, headers= headers)
        soup = BeautifulSoup(page.content, "lxml")
        articles = soup.find_all("div", attrs= {"class": "entry-content"})
        for article in articles:
            p_articles = article.find_all("p")
            for p_tags in p_articles:
                p_text = p_tags.get_text()
                article_column.append(p_text)
                
def create_excel():
    df_general = pd.DataFrame({"Links": links_column,
                            "Title": title_column})
    df_general.to_csv("datasets/data.csv")
    df_article = pd.DataFrame({"Article" : article_column})
    df_article.to_csv("datasets/data_article.csv")
