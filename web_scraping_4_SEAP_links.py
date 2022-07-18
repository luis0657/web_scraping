
#Automatically extract information from a Web page
#Requests
#Beautiful Soup
#

from cgitb import text
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

url1 = "C:/Users/gap1tl/Documents/git/web_scraping/SE1_SE3.html"

url2= "C:/Users/gap1tl/Documents/git/web_scraping/SE4_QGC4.html"

#We use get to download the contents of the webpage in text format
#and store in a variable called data:
#data  = requests.get(url).text 

with open(url1,'r') as f1:
    data1=f1.read()

with open(url2,'r') as f2:
    data2=f2.read()

soup = BeautifulSoup(data1,"html.parser")  # create a soup object using the variable 'data'

for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))


soup2 = BeautifulSoup(data2,"html.parser")  # create a soup object using the variable 'data'

for link in soup2.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))



# for link in soup.find_all('img'):# in html image is represented by the tag <img>
#     print(link)
#     print(link.get('src'))