# SXS💼🏃👨‍🎓
> 爬取实习僧网站数据分析岗位的数据并进行分析

![](https://img.shields.io/badge/python%20-3.6-brightgreen.svg) ![](https://img.shields.io/badge/build-passing-green.svg) ![](https://img.shields.io/badge/author-Chase%20Huang-yellowgreen.svg)

------

**本项目通过从实习僧网站上爬取全国数据分析实习生岗位的招聘信息475条，从而分析出目前全国的数据分析实习生大致的就业环境。**

**爬取思路：**

因为通过网页端获取的实习僧官网数据对前端渲染的数据进行了加密，且解密的过程非常繁琐，因此，从移动端入手，通过对应用程序进行抓包的方式
获得对应的数据。

本次通过抓取实习僧微信小程序的数据流获得数据（也可以对实习僧的APP进行抓包）

**主要分析以下问题：**
1. 数据分析实习生职位城市需求分析？
2. 数据分析实习生职位公司需求分析？
3. 哪些公司的数据分析实习生岗位相对较轻松(工资高，一周上班时间少)？
4. 数据分析实习生的文凭要求？

#### 文件介绍：
- `shixiseng.py`：实习僧数据爬取
- `数据分析实习生需求分析.ipynb`：对全国的数据分析实习岗位情况进行分析

#### 数据(data/)
- **sxs_数据分析.csv**：实习僧全国数据分析实习生招聘数据

#### 运行环境
- python3.6
- Fiddler(用于抓包)
- 夜神模拟器(用于模拟手机的操作)

#### 需要安装的包
- requests
- pandas
- numpy
- pyecharts
- matplotlib
- seaborn



