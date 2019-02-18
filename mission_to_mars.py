
# coding: utf-8

# In[303]:


from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd
import os


# In[304]:


url = "https://mars.nasa.gov/news/"
response = requests.get(url)
soup_news = BeautifulSoup(response.text, 'html.parser')
#print(soup_news)


# In[305]:


news_title = []
news_p = []

for item in soup_news.find_all('div', class_='slide'):
    try:
        news_head =  item.find("div", class_="content_title").text
        #print(f"News:{news_head}")
        news_title.append(news_head)
        
        paragraph= item.find("div", class_="rollover_description_inner").text
        #print(f"Paragraph: {paragraph}")
        news_p.append(paragraph)

    except Exception as e:
        print(e)
        
print(f"All titles: {news_title}")        
print(f"All Paragraphs: {news_p}")


# In[306]:


image_url ="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


# In[307]:


response = requests.get(image_url)
soup_image = BeautifulSoup(response.text, 'html.parser')

#print(response.text)


# In[308]:


featured_image_url = []
for item in soup_image.find_all('div', class_="grid_layout"):
#for item in soup.find_all('div'):
    for item1 in item.find_all('ul', class_="articles"):
        for result in item1.find_all('li', class_="slide"):
            image_src= "https://www.jpl.nasa.gov" + result.find('a', class_="fancybox")["data-fancybox-href"]
            featured_image_url.append(image_src)
            
print(f"Featured_image_url: {featured_image_url}")            


# In[309]:


weather_url = "https://twitter.com/marswxreport?lang=en"
response = requests.get(weather_url)
soup_weather = BeautifulSoup(response.text, "html.parser")
#print(soup_weather)


# In[310]:


mars_weather = []

for level_1 in soup_weather.find_all('ol', class_="stream-items js-navigable-stream"):
    for level_2 in level_1.find_all('li'):
        for level_3 in level_2.find_all('div', class_="content"):
            for header in level_3.find_all('div', "stream-item-header"):
                header_text = ''.join([x for x in header.span.text if x.isprintable() ])        
                if (header_text== "Mars Weather"):
                    # if collect only Mars Weather tweets
                    for item in level_3.find_all('div', class_="js-tweet-text-container"):
                        for result in item.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
                            mars_weather.append(result)
print(f"Mars Weather: {mars_weather}")                            


# In[311]:


facts_url = "https://space-facts.com/mars/"
response = requests.get(weather_url)
tables = pd.read_html(facts_url)
tables


# In[312]:


type(tables)
df = tables[0]
df.head(100)


# In[313]:


html_table = df.to_html()
html_table


# In[314]:


html_table.replace('\n', '')


# In[317]:


df.to_html('mars_fact.html')

