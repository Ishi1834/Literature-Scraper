import requests
import random 
from bs4 import BeautifulSoup
import time
from create_headers import process_headers

headers_list = process_headers()
def create_soup(link):
    #Pick a random browser headers
    headers = random.choice(headers_list)
    #Create a request session
    r = requests.Session()
    r.headers = headers
    response = r.get(link)
    time.sleep(5) # will sleep 5 sec after each request so the site doesn't respond with error 403
    print(str(response)) #this print allows for this function to be tested
    
    
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return soup