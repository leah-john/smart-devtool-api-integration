import requests
from bs4 import BeautifulSoup


def crawl_documentation(url):
    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return f"Failed to fetch page. Status Code: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator="\n", strip=True)
        print("\n===== SCRAPED TEXT =====")
        print(text[:1000])
        return text[:3000]
        
    except Exception as e:
        return f"Error: {str(e)}"
    