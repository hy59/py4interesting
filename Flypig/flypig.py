'''
@Description: get data from https://www.fliggy.com
@Author: Chase Huang
@Date: 2019-06-09 16:44:23
@LastEditTime: 2019-06-12 16:42:29
'''

import requests
import time
import random
import pandas as pd


class FlyPig(object):
    def __init__(self):
        self.cities = list(pd.read_csv('data/city_data.csv')['city'])

    def get_data(self):
        for city in self.cities:
            print('正在爬取城市: {} 的数据'.format(city))
            try:
                res = requests.get(
                    'https://travelsearch.fliggy.com/async/queryItemResult.do?searchType=product&keyword={}&category=SCENIC&pagenum=1'
                    .format(city))
                data = res.json()
                itemPagenum = data['data']['data'].get('itemPagenum')
                if itemPagenum is not None:
                    page_num = itemPagenum['data']['count']
                    for page in range(1, page_num + 1):
                        res = requests.get(
                            'https://travelsearch.fliggy.com/async/queryItemResult.do?searchType=product&keyword={}&category=SCENIC&pagenum={}'
                            .format(city, page))
                        data = res.json()

                        data_list = data['data']['data']['itemProducts'][
                            'data']['list'][0]['auctions']

                        for i in range(len(data_list)):
                            title = data_list[i]['fields']['title']
                            soldRecentNum = data_list[i]['fields'][
                                'soldRecentNum']
                            discountPrice = data_list[i]['fields'][
                                'discountPrice']
                            price = data_list[i]['fields']['price']

                            save_data = pd.DataFrame({
                                'city': [city],
                                'title': [title],
                                'soldRecentNum': [soldRecentNum],
                                'discountPrice': [discountPrice],
                                'price': [price],
                            })

                            self.save_data(save_data, page)
                        time.sleep(random.randint(1, 2))
                        print('成功爬取城市:{}的第{}页数据!'.format(city, page))
                        
            except Exception:
                continue

    @staticmethod
    def save_data(save_data, page):
        if page == '1':
            save_data.to_csv(
                'data/flypig.csv', index=False, mode='a', header=True)
        else:
            save_data.to_csv(
                'data/flypig.csv', index=False, mode='a', header=False)


if __name__ == "__main__":
    FP = FlyPig()
    FP.get_data()
    print('\nDone...')