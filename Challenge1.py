from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
#import pandas as pd

a = False #boolean variable 


while (a = False): #While loop to ensure that the process infinitely loops
  imp = input("Please input the email credentials \n") #Take the input of the email id from the user
  link = "https://www.ecs.soton.ac.uk/people/" + imp #Format the weblink 
  source = urllib.request.urlopen(link).read() #Access the website via urllib
  soup = BeautifulSoup(source,'lxml') #Extract the sources from the ecs website  
  name = str(soup.title) #Extract the title of the webpage, the only bit of infomation we need.
  namelist = name.split("|") #convert the string "name" into a list to seperate the data for output
  print("This is " + (namelist[0])[7:-1] + "! Working at the School of" + namelist[1] + 'at the University') #Outputs the infomation provided from the webscarper, assuming access to the website is correct.
#If the input is invalid then the program will just simpily crash :)
