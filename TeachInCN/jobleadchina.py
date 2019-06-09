'''
@Author: Chase Huang
@Date: 2019-06-05 15:26:47
@LastEditTime: 2019-06-09 16:04:51
@Description: get the data from the jobleadchina website
'''
import requests
import pandas as pd
from lxml import etree


class JobLeadChina(object):
    def __init__(self, last_page):
        self.start_urls = [
            'http://jobleadchina.com/job?job_industry=Teaching&company_name=&page={}'
            .format(page) for page in range(1, last_page + 1)
        ]

    def get_data(self):
        for url in self.start_urls:
            res = requests.get(url)
            page = url.split('=')[-1]
            self.parse_data(res, page)
            print("Get data from page {} successful!".format(page))

    @staticmethod
    def parse_data(res, page):
        if res.status_code == 200:
            parsed = etree.HTML(res.text)

            title = parsed.xpath('//*[@class="positionTitle"]/a/text()')
            link = parsed.xpath('//*[@class="positionTitle"]/a/@href')
            salary = [
                slr.strip()
                for slr in parsed.xpath('//*[@class="salaryRange"]/text()')
            ]
            company = parsed.xpath('//*[@class="companyName"]/a/text()')
            com_type = parsed.xpath(
                '//*[@class="jobThumbnailCompanyIndustry"]/span[1]/text()')
            area = parsed.xpath(
                '//*[@class="jobThumbnailCompanyIndustry"]/span[3]/text()')
            post_time = parsed.xpath('//*[@class="post-time"]/text()')
            exp_level = parsed.xpath(
                '//*[@class="jobThumbnailPositionRequire"]/span[3]/text()')
            edu_level = parsed.xpath(
                '//*[@class="jobThumbnailPositionRequire"]/span[1]/text()')
            job_type = parsed.xpath(
                '//*[@class="jobThumbnailPositionRequire"]/span[5]/text()')

            data = pd.DataFrame({
                'title': title,
                'link': link,
                'salary': salary,
                'company': company,
                'com_type': com_type,
                'area': area,
                'post_time': post_time,
                'exp_level': exp_level,
                'edu_level': edu_level,
                'job_type': job_type
            })

            if page == '1':
                data.to_csv(
                    'data/jobleadchina.csv',
                    index=False,
                    mode='a',
                    header=True)
            else:
                data.to_csv(
                    'data/jobleadchina.csv',
                    index=False,
                    mode='a',
                    header=False)

        else:
            print("Can't request {}".format(res.url))


if __name__ == "__main__":
    JLC = JobLeadChina(105)
    JLC.get_data()
    print("All done ...")