import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Example: Scraping article titles from a news website
            article_titles = soup.find_all('h2', class_='accordion-header')
            for title in article_titles:
                print(title.text.strip())
        else:
            print("Failed to fetch the page:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    url = "https://cyberadda.tech/"  # Replace with the URL of the website you want to scrape
    scrape_website(url)
