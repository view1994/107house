import time
from room_info import roomInfo
from urls import url_list

while True:
    print('collect '+str(url_list.count())+' urls and '+str(roomInfo.count())+' room info, and there are '+
          str(len(set([i['url'] for i in url_list.find()])-set([i['url'] for i in roomInfo.find()])))+' rest!')
    time.sleep(5)