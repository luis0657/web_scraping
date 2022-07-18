import json
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd
import time


url = "https://en.wikipedia.org/wiki/List_of_largest_banks"

dataframe_list = pd.read_html(url, flavor='bs4')

dataframe_list_10_most_dense=pd.read_html(url, flavor='bs4')[3]

json_info=dataframe_list_10_most_dense.to_json()

with open('banks.json','w') as f:
    json.dump(json_info,f)