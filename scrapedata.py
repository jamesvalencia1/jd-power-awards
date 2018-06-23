# -*- coding: utf-8 -*-
"""
@author: James Valencia
@description: This code will scrape a website based on certain parameters in the code.
              It is a simple example of how to use BeautifulSoup for scraping web data.
"""

## Below are the required modules needed to run the program
import requests
from bs4 import BeautifulSoup

## This will get the website data and store as the 'resp' variable
resp = requests.get('http://www.jdpower.com/cars/awards/vehicle-dependability-study')

## This will store the source code of the website to the 'txt' variable
txt = resp.text

## This will utilize the BeautifulSoup function to deconstruct the source code to the 'soup' variable
soup = BeautifulSoup(txt, 'html.parser')

## This will locate all the text that fall under a certain class name under the 'div' html tags
awardees = soup.find_all('div', {'class' : 'awardee-model'}, text=True)

## This will print each item to the console
for item in awardees:
    print(item.text)
    
## With the 'awardees' variable you can convert it to a list or make it a dataframe with pandas