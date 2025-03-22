from bs4 import BeautifulSoup
import requests
url = "https://github.com/trending"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    repos = soup.find_all('h1')
    for repo in repos:
        print(repo.text.strip())
else:
    print("Failed to fetch the URL")