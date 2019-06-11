'''
@Author: Chase Huang
@Date: 2019-06-05 16:43:42
@LastEditTime: 2019-06-10 10:11:13
@Description: get the local englisgh teacher job data from job910.com
'''
import requests
import time
import random
import pandas as pd
from lxml import etree


class Job910(object):
    def __init__(self, last_page):
        self.headers = {
            "Accept":
            "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            "Accept-Encoding":
            "gzip, deflate",
            "Connection":
            "keep-alive",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }
        self.start_urls = [
            'http://www.job910.com/search.aspx?keyword=英语教师&pageSize=20&pageIndex={}'
            .format(i) for i in range(1, last_page + 1)
        ]

    def get_data(self):
        for url in self.start_urls:
            res = requests.get(url, headers=self.headers)
            page = url.split('=')[-1]
            self.parse_data(res, page)
            print("Get data from page {} successful!".format(page))
            time.sleep(random.randint(1, 2))

    @staticmethod
    def parse_data(res, page):
        if res.status_code == 200:
            parsed = etree.HTML(res.text)

            title = parsed.xpath('//*[@class="position title"]/a/text()')
            link = parsed.xpath('//*[@class="position title"]/a/@href')
            salary = parsed.xpath('//*[@class="salary title"]/text()')
            company = parsed.xpath('//*[@class="com title adclick"]/text()')
            area = parsed.xpath('//*[@class="area title2"]/text()')
            post_time = parsed.xpath('//*[@class="time title2"]/text()')
            exp_level = parsed.xpath('//*[@class="exp title2"]/text()')

            data = pd.DataFrame({
                'title': title,
                'link': link,
                'salary': salary,
                'company': company,
                'area': area,
                'post_time': post_time,
                'exp_level': exp_level
            })

            if page == '1':
                data.to_csv(
                    'data/job910.csv', index=False, mode='a', header=True)
            else:
                data.to_csv(
                    'data/job910.csv', index=False, mode='a', header=False)
        else:
            print("Can't request {}".format(res.url))


if __name__ == "__main__":
    J = Job910(392)
    J.get_data()
    print("All done ...")