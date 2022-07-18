from wsgiref import headers
import requests

url='https://www.ibm.com/'

r=requests.get(url)

print(r.status_code) # Status code, 200 if ok. 400 if not

header=r.headers # Dictionary with the header info
print(header['date']) # Date 
print(header['Content-Type']) # Content Type
print(r.text[0:200]) # get the body of the web in HTML

url_get='http://httpbin.org/get'

payload={"name":"Joseph","ID":"123"}

r=requests.get(url_get,params=payload)

print(r.url)

print(r.text)

print(r.json())


url_post='http://httpbin.org/post'

r_post=requests.post(url_post,data=payload)



