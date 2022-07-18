

#Automatically extract information from a Web page
#Requests
#Beautiful Soup
#

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"


two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

two_tables_bs.find("table")

pizza_table=two_tables_bs.find("table",class_='pizza')

print(pizza_table)