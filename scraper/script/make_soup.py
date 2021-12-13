import requests
import random 
from bs4 import BeautifulSoup
import time
from script.create_headers import process_headers 

headers_list = process_headers()
def create_soup(link):
    #Pick a random browser headers
    headers = random.choice(headers_list)
    response = requests.get(link, headers) 
    #will sleep 5 sec after each request so the site doesn't respond with error 403
    time.sleep(5)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    return soup