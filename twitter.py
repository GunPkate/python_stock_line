from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time

driverpath = r'C:\Users\Gun\Desktop\Projects\Python Bootcamp\chromedriver.exe'

opt = webdriver.ChromeOptions() #hide googledriver
opt.add_argument('headless')
driver = webdriver.Chrome(driverpath,options=opt)

def TwitterPost(twitter_name):
    url = 'https://twitter.com/{}'.format(twitter_name)

    driver.get(url)
    time.sleep(4) #delay 4 sec to load twitter post
    
    pixel = 0
    for i in range(8):
        driver.execute_script('window.scrollTo(0,{})'.format(pixel))
        time.sleep(4)
        if i <=3:
            pixel =pixel + 1000
        elif i <=6:
            pixel =pixel + 2000
        else: pixel =pixel + 10000 
        
    page_html = driver.page_source

    data = soup(page_html,'html.parser')
    post = data.find_all('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

    allpost = []
    founddot = False
    for p in post:
        txt = p.text
        if founddot == True:
            allpost.append(txt)
            # print(p.text)
            # print('---')
            founddot = False #reset

        if txt == '·':
            founddot = True
    return allpost

# TwitterPost('elonmusk')

#####

from songline import Sendline
token ='Qq2gIGImTe3zIZmQQgfwcJWmxGocEBEFpZyvzqxxdrv'
messenger = Sendline(token)

########
checktwiter = ['RioTinto','digitalrealty','amd','BAESystemsplc','cnnbrk']
for ct in checktwiter:
    texttoline = ''
    post = TwitterPost(ct)
    print('---{}---'.format(ct))
    texttoline +='---{}---\n'.format(ct)        
    for p in post:
        print(p)
        texttoline += p + '\n'
        print('---')
    messenger.sendtext(texttoline)
driver.close()

