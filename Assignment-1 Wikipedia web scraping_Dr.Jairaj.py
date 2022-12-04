#!/usr/bin/env python
# coding: utf-8

# # Web Scraping of wikipedia headers 
# 

# Import Required liberaries

# In[1]:


from bs4 import BeautifulSoup
import requests 
page=requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[2]:


soup=BeautifulSoup(page.content)
soup


# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# In[4]:


# import required modules
from bs4 import BeautifulSoup
import requests


# get URL
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
 
# create object
object = soup.find(id="mp-left")
 
# find tags
items = object.find_all(class_="mp-h2")
result = items[0]
 
# display tags
print(result.prettify())


# In[ ]:




