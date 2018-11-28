#coding utf-8
from bs4 import BeautifulSoup
import requests
import pymongo
import time
import random
client=pymongo.MongoClient('localhost',27017)
room107 =client['room107']
roomInfo=room107['room_info']
roomSaved=room107['room_info_saved']
wrong_list=[]
bad_url=[]

proxy_list = [
   # 'http://218.241.234.48:8080',
   # 'http://114.215.108.183:3128',
    'http://139.129.166.68:3128',

    #'http://49.85.4.28:20210',
    #'http://115.217.254.20:31199',
   # 'http://180.122.150.10:25648',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}

time_list=[1,2,3]
#t=random.choice(time_list)

def get_room_info(url):
    if url:
        webdata = requests.get(url,proxies={'http': 'http://114.93.111.153:9000'})#proxies={'http': random.choice(proxy_list)}
        if webdata.status_code == 404:
            print('url 404: '+url)
            bad_url.append(url)
            pass
        else:
            soup = BeautifulSoup(webdata.text, 'lxml')
            try:
                time.sleep(1)#random.choice(time_list)
                room_info = {
                    'monthPrice': soup.select('span.monthPrice')[0].get_text(),
                    'locations': soup.select('table.locations > tr > td > h1')[0].get_text().strip().split(),
                    'rooms': soup.select('table.allHouseCondition1')[0].get_text().strip().split(),
                    'area': soup.select('table.allHouseCondition2')[0].get_text().strip().split(),

                    'date': soup.select('div.houseDetail > table > tr:nth-of-type(2) > td:nth-of-type(2)')[0].get_text(),
                    'url':url
                }
                roomInfo.insert_one(room_info)
            except :
                print('get room info error from'+url)
                wrong_list.append(url)
    else:
        pass

print('got room_info : '+str(roomInfo.count()))
print('saved roome info '+str(roomSaved.count()))

'''
if __name__ == '__main__':
    proxy_list = [
        'http://117.177.250.151:8081',
        'http://111.85.219.250:3129',
        'http://122.70.183.138:8118',
    ]
    proxy_ip = random.choice(proxy_list)  # 随机获取代理ip
    proxies = {'http': proxy_ip}
    url='http://www.107room.com/z2_a1-h2_51'
    webdata = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(webdata.text, 'lxml')
    print(webdata)

'''