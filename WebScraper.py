import requests
from bs4 import BeautifulSoup, Comment
import re

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = [a["href"] for a in soup.find_all("a", href=True)]
comments = [comment for comment in soup.find_all(string=lambda text: isinstance(text, Comment))]
emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))

print("Links:", links)
print("Comentarios:", comments)
print("Correos electronicos:", emails)