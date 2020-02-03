# _*_ coding:utf-8 _*_
import requests
import re
from bs4 import BeautifulSoup


# 从第一张开始
url = "http://m.5k5m.com/book/327836/80015755.html"
chapter_url = "http://m.5k5m.com"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"

headers = {
    "User-Agent":user_agent
}
fb = open('某某.txt','w', encoding='utf-8')

response = requests.get(url,headers = headers)
response.encoding = 'utf-8'
# HTML内容
html = response.text
bs = BeautifulSoup(html,"html.parser")
# 文章正文
content = bs.select("div[class='chapter']")[0].get_text()
print("写入%s......"%bs.h3.string)
fb.write(content)
fb.write("\n")
a = bs.select('a[id="btnNext"]')[0].get("href")

while a != "/book/327836/91941167.html?page=5":
    response = requests.get(chapter_url+a, headers=headers)
    response.encoding = 'utf-8'
    # HTML内容
    html = response.text
    bs = BeautifulSoup(html, "html.parser")
    # 文章正文
    content = bs.select("div[class='chapter']")[0].get_text()
    print("写入%s......" % bs.h3.string)
    fb.write(content)
    fb.write("\n")
    a = bs.select('a[id="btnNext"]')[0].get("href")


# # 获取章节内容
# def get_chapter_context(url):
#     chapter_content = ""
#     # 假设有三页
#     res = requests.get(url,headers=headers)
#     res.encoding = "utf8"
#     chapter_bs = BeautifulSoup(res.content,"html.parser")
#     # 这是此页的正文
#     chapter_content = chapter_content + chapter_bs.find(class_="chapter").get_text()
#     return chapter_content
#
# fb.write(get_chapter_context(chapter_urls))
# fb.write("\n")

