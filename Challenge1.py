from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd



imp = input("Please input the email credentials \n")
link = "https://www.ecs.soton.ac.uk/people/" + imp
source = urllib.request.urlopen(link).read()
soup = BeautifulSoup(source,'lxml')
name = str(soup.title)
namelist = name.split("|")
print("This is " + (namelist[0])[7:-1] + "! Working at the School of" + namelist[1] + 'at the Un')
