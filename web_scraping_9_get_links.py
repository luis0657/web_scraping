
#Automatically extract information from a Web page
#Requests
#Beautiful Soup

from cgitb import text
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

url = "https://seap.com"

#We use get to download the contents of the webpage in text format
#and store in a variable called data:
data  = requests.get(url).text 


soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'

for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))