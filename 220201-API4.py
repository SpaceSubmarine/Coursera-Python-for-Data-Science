from tkinter.font import BOLD
import requests
import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

print("STATUS:", r.status_code)
print("\nREQUEST HEADERS:", r.request.headers)
print("\nrequest body:", r.request.body)

header=r.headers
print("\nHTTP RESPONSE HEADERS:", r.headers)

print("\nDATE:", header['date'])
print("\nContent-Type:", header['Content-Type'])
print("\nENCODING:", r.encoding) 

print("\nFIRST 100 CHARACTERS IN THE HTML BOODY:", r.text[0:100])

#You can load other types of data for non-text requests, like images. Consider the URL of the following image:
# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'
r=requests.get(url)

#We can look at the response header:
print("\nHTTP RESPONSE HEADERS:", r.headers)
print("\nCONTENT TYPE:", r.headers['Content-Type'])

#=====================================================
#An image is a response object that contains the image as a bytes-like object.
#As a result, we must save it using a file object. First, we specify the file path and name:
path=os.path.join(os.getcwd(),'image.png')
path
#We save the file, in order to access the body of the response we use the 
#attribute content then save it using the open function and write method:
with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)