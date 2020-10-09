#install packages
pip install selenium # installed for webscraping
pip install twilio # installed for sending notifications

#import packages
from selenium import webdriver
import itertools as it
from twilio.rest import Client
import os

#url to scrape
url = "https://www.uoftengcareerportal.ca/students/login.htm"
nop_list = []

#function to return current number of open positions
def get_positions(url):
    chromedriver = "C:/Users/Anubhav Sharma/Desktop/chromedriver"
    username = ''
    password = ''
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    driver.find_element_by_id('j_username').send_keys(username)
    driver.find_element_by_id('j_password').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/input').click()
    driver.find_element_by_xpath('//*[@id="mainContentDiv"]/div[2]/div/div[1]/div/a[2]').click()
    driver.find_element_by_xpath('//*[@id="searchPostings"]/div[2]/div/ul/li/a').click()
    text = driver.find_element_by_xpath('//*[@id="dashboard"]/div[2]/div[1]/a')
    text = text.text
    number_of_positions = int(text.split(' ')[0])
    return number_of_positions

#Twilio API to send notifications
def call_twilio(Message):
    account_sid = os.environ['account_sid']
    auth_token = os.environ['auth_token']
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=Message, from_='+19166650472', to='+16478335197')
    return 'message sent'

first_nop = get_positions(url)
nop_list = []
nop_list.append(str(first_nop))

if len(nop_list)>=2:
    if nop_list[-1]>nop_list[-2]:
        new_pos = int(nop_list[-1])-int(nop_list[-2])
        new_pos = str(new_pos)
        message = 'There are {} new positions'.format(new_pos)
        result = call_twilio(message)
        print(result)
    else:
        result = call_twilio('No New Positions, sorry')
        print(result)


# In[73]:


print(nop_list)


# In[54]:




