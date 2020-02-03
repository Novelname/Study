# _*_ coding:utf-8 _*_
import requests
import re
from bs4 import BeautifulSoup

# http://m.5k5m.com/book/426380/0/1.html 整个目录页
url = "http://m.5k5m.com/book/426380/0/1.html"
chapter_url = "http://m.5k5m.com"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"

headers = {
    "User-Agent":user_agent
}

response = requests.get(url,headers = headers)
response.encoding = 'utf-8'

# HTML内容
html = response.text

bs = BeautifulSoup(html,"html.parser")
title = bs.title.string[0:9]
# 文章标题 print(title)

# 将文件写入
fb = open('%s.txt'% title,'w', encoding='utf-8')

# 装有所有的章节 chapterlist div
chapter_div = bs.find(id="chapterlist")
# bs的根据css查找,find_all是查找所有,返回的是一个list
chapter_divs = bs.find_all(class_="dc-cap")
# chapter_as = re.findall(r'<a href="(.*?)">(.*?)</a>',chapter_divs)
# print(chapter_as)

# 获取章节内容
def get_chapter_context(url):
    chapter_content = ""
    # 假设有三页
    for i in range(1,4):
        res = requests.get(url+"?page="+str(i),headers=headers)
        res.encoding = "utf8"
        chapter_bs = BeautifulSoup(res.content,"html.parser")
        # 这是此页的正文
        chapter_content = chapter_content + chapter_bs.find(class_="chapter").get_text()
    return chapter_content



# 获取章节url
for chapter in chapter_divs:
    # [<a href = "/book/426380/92060044.html" >第69章番外 < / a >]
    # 获取到href print(re.findall(r'href="(.*?)"', str(chapter.select('a')[0])))
    chapter_urls = chapter_url + chapter.select('a')[0].get("href")
    # print(chapter_urls)
    # 获取章节(第几章)
    chapter_title = chapter.select('a')[0].string
    print("-------准备写入:%s--------"%chapter_title.replace(" ","").replace("\n",""))
    # chapter_href,chapter_title=re.findall(r'<ahref="(.*?)" >(.*?)</a>', str(chapter.select('a')[0]).replace(' ',''))
    fb.write(get_chapter_context(chapter_urls))
    fb.write("\n")


'''
# <meta property="og:title" content="上门龙婿" />
title = re.findall(r'<meta property="og:title" content="(.*?)" />',html)[0]

fb = open('%s.txt'% title, 'w',encoding='utf-8')

# 获取章节
dl = re.findall(r'<dl class="panel-bodyljMhaU panel-chapterlistljMhaU" style="margin-bottom: 0;padding-top: 0;padding: 15px;>.*?</div>',html,re.S)
chapter_info_list = re.findall(r'<a href="(.*?)" title="(.*?)">(.*?)</a>',dl)

print (chapter_info_list)


for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url = "https://www.biqugeso.com/book/47358/%s" % chapter_url
    chapter_url = chapter_url.replace(' ','')

    chapter_response = requests.get(chapter_url,headers = headers)
    chapter_response.encoding = 'utf8'
    chapter_html = chapter_response.text

    chapter_content = re.findall(r'<div id="content">(.*?)</div>',chapter_html,re.S)[0]

'''

# title_meta = bs(property = "og:novel:book_name") [<meta content="上门龙婿" property="og:novel:book_name"/>]
# title1 = re.findall(r'<meta property="og:novel:book_name" content="(.*?)" />',title_meta)

# print (title1)
# print (title) <title>上门龙婿(叶辰)免费阅读最新章节-笔趣阁</title>
# print (title.string) 上门龙婿(叶辰)免费阅读最新章节-笔趣阁
# print (title.name)   title
# print (bs.head)