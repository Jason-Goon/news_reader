# scripts/content_aggregator.py

import requests
from bs4 import BeautifulSoup
import re

def fetch_news():
    RSS_URL = "http://feeds.bbci.co.uk/news/rss.xml"

    try:
        response = requests.get(RSS_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

    soup = BeautifulSoup(response.content, features="xml")
    items = soup.findAll('item')

    if not items:
        print("No news items found.")
        return []

    news_list = []
    for news_item in items:
        guid = news_item.guid.text if news_item.guid else news_item.link.text
        title = news_item.title.text
        description = news_item.description.text

        full_text = f"{title}. {description}"
        summarized_text = summarize_text(full_text)

        news_list.append((guid, summarized_text))

    return news_list

def summarize_text(text):
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    sentences = [s.strip() for s in sentences]
    summary_sentences = sentences[:2]
    summary = ' '.join(summary_sentences)
    if not summary.endswith('.'):
        summary += '.'
    return summary
