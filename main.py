#coding:utf-8
from multiprocessing import Pool
import time
from urls import url_list
from room_info import get_room_info,roomInfo,wrong_list,bad_url
def get_rest_urls():
    db_urls = [i['url'] for i in url_list.find()]
    info_urls = [i['url'] for i in roomInfo.find()]
    x = set(db_urls)
    y = set(info_urls)
    rest_urls = x - y
    print('rest urls:'+str(len(rest_urls)))
    return list(rest_urls)

if __name__ == '__main__':

    pool = Pool(processes=6)
    pool.map(get_room_info,get_rest_urls())
    pool.close()
    pool.join()
    print('got urls numbers: '+str(url_list.count()))
    print('bad urls numbers: ' + str(len(bad_url)))
    print('save room info success: '+str(roomInfo.count()))
    print('get room info failed numbers: ' + str(len(wrong_list)))
'''
    for url in rest_urls:
    get_room_info(url)

    get_url_list()
    get_all_info()





'''