#coding:utf-8
from bs4 import BeautifulSoup
import requests
import time
import pymongo

client=pymongo.MongoClient('localhost',27017)
room107 =client['room107']
url_list=room107['url_list']

def get_url_list():
    url_host="http://www.107room.com"
    for n in range(1,1000):#401
        url_page=url_host+'/z2_a1-h2_'+str(n)
        print('get url from  '+url_page)
        web_data=requests.get(url_page)
        if web_data.status_code==404:
            print('scrapping urls end!!\ntotally scraped '+str(n-1)+' pages urls!')
            break
        else:
            soup=BeautifulSoup(web_data.text,'lxml')
            for item in soup.select('div.oneHouse.setStyle > a'):
                url_list.insert_one({'url':url_host+item.get('href')})
            time.sleep(1)

#get_url_list()
print('got '+str(url_list.count())+' urls!')