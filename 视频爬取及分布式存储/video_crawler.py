"""
@Coding: uft-8
@Time: 2020/3/23 16:55
@Author: Ryne Chen
@File: video_crawler.py 
@Python Version: 3.7
"""

import requests
from bs4 import BeautifulSoup
import re


def crawler(url):
    # 设置请求头部
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

    # 获取网页对象
    resource = requests.get(url, headers=headers)

    # 获取文本信息
    html = resource.text

    # 生成一个soup对象
    soup = BeautifulSoup(html, 'lxml')

    # 获取源代码中所有的video标签对象
    net_url = soup.find_all('video')

    # print(net_url)

    # 定义网络视频地址数组
    video_url = []

    for i in net_url:
        if i.get('src') is not None:
            # print(i.get('src'))

            # 获取video标签的src属性，拼接上 https:
            video_url.append('https:' + i.get('src'))

    # print(video_url)

    # 获取视频名称
    # 正则表达式获取要解析的视频名称
    titles = re.findall('pr-data-title="(.*?)">', html)

    # print(titles)

    # 下载视频文件：将视频名称和视频地址一一对应
    for t, v in zip(titles, video_url):
        with open('./data/' + t + '.mp4', 'wb') as f:
            f.write(requests.get(v).content)


def run():
    # 视频网站url地址
    url = 'https://ibaotu.com/shipin/7-0-0-0-3-1.html'

    print('开始下载...')
    crawler(url)
    print('下载完毕~')


if __name__ == '__main__':
    run()
