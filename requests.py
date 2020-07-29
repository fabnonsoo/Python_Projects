# EXAMPLE 1:- To get the source of a website in python....
import requests

r = requests.get('https://xkcd.com/353/')

print(dir(r))
print(r.text)        # This line produces the HTML of that page..


# EXAMPLE 2:- To GET AN IMAGE FROM THE WEB IN PYTHON.....
import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(dir())               # Gives the attributes we can use for the response object...
print(r.content)           # Doesn't o/p the image but only the content of the response object..

r = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('csimage.png', 'wb') as f:         # Saves the content of the Image in a python directory in our computer
    f.write(r.content)


# EXAMPLE 3:- To CHECK/GET THE NUMBER/TYPE OF RESPONSE GOTTEN FROM THE SITE..
# The following are HTTP Status codes:...
# The 200 = Success!
# The 300 = These are re-directs
# The 400 = Client Errors - You're trying to access a page whithout permission!
# THE 500 = Server Errors - Errors you see when a site crashes!

import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.status_code)
print(r.ok)              # Means the reponse from the site is TRUE(No Errors)
print(r.headers)         # Gives us the headers that come w/the website..


# EXAMPLE 4:- USING REQUESTS TO PASS IN SOME URL PARAMETERS.....
import requests

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.text)               # Outputs response from the url - httpbin.org
print(r.url)                # Outputs the url parameters that was requested..


# EXAMPLE 5:- POST Data TO A CERTAIN URL....
import requests

payload = {'username': 'nonso', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
print(r.json())        # Outputs a python dict from the json response

r_dict = r.json()
print(r_dict['form'])


# EXAMPLE 6:- PASSING CREDENTIALS FOR BASIC AUTHENTICATION IN PYTHON....
import requests

r = requests.get('http://httpbin.org/basic-auth/nonso/testing', auth=('nonso', 'testing'))
print(r)
print(r.text)


# EXAMPLE 7:- SETTING TIMEOUT WHEN A WEBSITE ISN'T RESPONDING/NOT GETTING A URL RESPONSE ON TIME.....
import requests

r = requests.get('http://httpbin.org/delay/6', timeout=4)
print(r)
