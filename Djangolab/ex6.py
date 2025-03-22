from bs4 import BeautifulSoup
import requests
url = "https://www.coursera.org"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
courses = soup.find_all('h2')
for course in courses:
    print(course.text)
