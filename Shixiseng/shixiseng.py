'''
@Description: get the data from wechat small program shixiseng
@Author: Chase Huang
@Date: 2019-06-09 16:06:49
@LastEditTime: 2019-06-14 20:09:45
'''
import requests
import pandas as pd
from lxml import etree


class Shixiseng(object):
    def __init__(self, city, keyword, num_page):
        self.start_urls = [
            'https://mina.shixiseng.com/mina/interns/search?k={}&c={}&i=&page={}'
            .format(keyword, city, i) for i in range(1, num_page + 1)
        ]
        self.city = city
        self.keyword = keyword

    def get_data(self):
        for url in self.start_urls:
            res = requests.get(url)
            page = url.split('=')[-1]
            self.parse_data(self, res, page)
            print("Get data from page {} successful!".format(page))

    def parse_data(self, res, page):
        data_list = res.json()['msg']
        if data_list is not None:
            for i in range(len(data_list)):
                uuid = data_list[i]['uuid']
                job_name = data_list[i]['name']
                minsal = data_list[i]['minsal']
                maxsal = data_list[i]['maxsal']
                company = data_list[i]['cname']
                city = data_list[i]['city']
                day = data_list[i]['day']

                # get job desc and degree
                desc, degree = self.get_desc(uuid)

                data = pd.DataFrame({
                    'uuid': [uuid],
                    'job_name': job_name,
                    'minsal': minsal,
                    'maxsal': maxsal,
                    'company': company,
                    'city': city,
                    'day': day,
                    'desc': [desc],
                    'degree': degree
                })

                data.to_csv(
                    'data/sxs_{}.csv'.format(self.keyword),
                    index=False,
                    mode='a',
                    header=False)

        else:
            print("Can't request {}".format(res.url))

    @staticmethod
    def get_desc(uuid):
        url = 'https://www.shixiseng.com/intern/{}'.format(uuid)
        res = requests.get(url)
        parsed = etree.HTML(res.text)
        desc = parsed.xpath("//*[@class='job_detail']/p/text()")
        try:
            degree = parsed.xpath("//span[@class='job_academic']/text()")[0]
        except IndexError:
            degree = '不限'
        return desc, degree


if __name__ == "__main__":
    city = '全国'
    keyword = '数据分析'
    num_page = 24
    SXS = Shixiseng(city, keyword, num_page)
    SXS.get_data()

    print("\nGet job {} in {} data success!".format(keyword, city))
