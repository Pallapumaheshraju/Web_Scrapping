import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=headers)
print(response)