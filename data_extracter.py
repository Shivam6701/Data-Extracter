from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:/Users/dell/webdriver/bin/chromedriver")


products=[]
prices=[]
rating = []
driver.get("https://www.flipkart.com/audio-video/headphones/boat~brand/pr?sid=0pm%2Cfcn&marketplace=FLIPKART&otracker=product_breadCrumbs_boAt+Headphones&sort=popularity")
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('div', attrs={'class':'_4ddWXP'}):
    name=a.find('a', attrs={'class':'s1Q9rs'})
    price=a.find('div', attrs={'class':'_30jeq3'})
    rat=a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    rating.append(rat.text)

df = pd.DataFrame({'Product Name':products,'Price':prices, 'Rating':rating})
df.to_csv('_flip2.csv', index=True, encoding='utf-8')