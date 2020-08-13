from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
BsObj = BeautifulSoup(html.read())
print(BsObj.h1)

from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd