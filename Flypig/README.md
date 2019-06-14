# FlyPig🐷🎠💸
> 分析全国景点的情况

![](https://img.shields.io/badge/python%20-3.6-brightgreen.svg) ![](https://img.shields.io/badge/build-passing-green.svg) ![](https://img.shields.io/badge/author-Chase%20Huang-yellowgreen.svg)

------

**本项目主要爬取飞猪网上全国的景点门票的数据共58,551条，并在此基础上对全国的景点情况进行分析：**

1. 哪些城市/省份的旅游选择最多？
2. 哪些城市最受游客青睐？
3. 最热门的景点
4. 打折力度最大的景点

#### 文件介绍：
- `flypig.py`：飞猪网站爬取
- `各地景点分析.ipynb`：对全国的景点数据进行分析

#### 数据(data/)
- **city_data.csv**：全国城市数据
- **flypig.csv**：飞猪网全国景点门票数据
- **json_find.txt**：需要爬取得属性的定位

#### 运行环境
- python3.6

#### 需要安装的包
- requests
- pandas
- numpy
- pyecharts

**注：本项目参考文章 [Alfred数据室](https://wx1.sinaimg.cn/mw690/007yVcwsgy1g03lo67ikoj30u00f0ta0.jpg)，阅读对应文章《[五一不看人人人人人人，哪儿耍合适？ ](https://mp.weixin.qq.com/s/iuCNreCuKzrggdXtvurpkQ)》**


**注：参考项目 https://github.com/Alfred1984/interesting-python/tree/master/LaborDay**

