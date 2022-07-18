from cgi import print_form
from distutils.util import run_2to3
from email import header
import requests
import os
from PIL import Image
from IPython.display import IFrame

# url_1='https://www.ibm.com/'
# r=requests.get(url_1)

# print(r.status_code)
# print(r.request.headers)
# print("request body:", r.request.body)
# header_1=r.headers
# print(r.headers)
# print(header_1['date'])
# print(header_1['Content-Type'])
# print(r.encoding)
# print(r.text[:50])  

# url_2='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
# r_2=requests.get(url_2)
# print(r_2.headers)
# print(r_2.headers['Content-Type'])

# path_1=os.path.join(os.getcwd(),'image.png')

# print(path_1)

# with open(path_1,'wb') as f:
#     f.write(r_2.content)


url_3='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
r_3=requests.get(url_3)
print(r_3.headers)
print(r_3.headers['Content-Type'])

path_1=os.path.join(os.getcwd(),'Example_1.txt')

print(path_1)

with open(path_1,'wb') as f:
    f.write(r_3.content)