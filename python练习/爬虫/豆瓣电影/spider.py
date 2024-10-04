# 写一个爬虫程序对豆瓣Top250的电影进行爬取
import os
import re
import urllib.request, urllib.error
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
from bs4 import BeautifulSoup
from xlwt.Utils import cell_to_packed_rowcol


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    askURL(baseurl)
    # 3.保存数据
    savepath = "豆瓣电影250_2.xls"
    savedata(savepath, datalist)


# 正则表达式
findlink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取的网页源码
    # 2.逐一解析数据
    soup = BeautifulSoup(html, "html.parser")  # html解析器
    for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表 要找到class=item 同时又是div的内容
        # print(item)
        data = []  # 保存一部电影的所有信息
        item = str(item)
        # link=re.findall(findlink,item)[0] #re库用来通过正则表达式查找指定的字符串  
        # data.append(link)
        # imgSrc=re.findall(findImgSrc,item)[0]#添加图片
        # data.append(imgSrc)
        titles = re.findall(findTitle, item)
        if (len(titles) == 2):
            ctitle = titles[0]  # 添加中文名
            data.append(ctitle)
            otitle = titles[1].replace("\xa0/\xa0", "")  # 去掉外文名中无关的符号
            data.append(otitle)  # 添加外文名
        else:
            data.append(titles[0])
            data.append('')  # 留空
        rating = re.findall(findRating, item)[0]
        data.append(rating)
        # judgeNum=re.findall(findJudge,item)[0]
        # data.append(judgeNum)
        inq = re.findall(findInq, item)
        if (len(inq) != 0):
            inq = inq[0].replace("。", ",")
            data.append(inq)
        else:
            data.append(" ")
        # bd=re.findall(findBd,item)[0]
        datalist.append(data)
    print(datalist)
    return datalist


# 得到制定一个URL的网页内容
def askURL(url):
    # 用户代理：表示告诉浏览器，我们是什么类型的机器
    # 模拟浏览器头部信息
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    # 携带head来访问浏览器
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def savedata(savepath, datalist):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('豆瓣电影', cell_overwrite_ok=True)
    col = ("电影中文名字", "电影外文名", "评分", "一句话简介")
    for i in range(0, 4):
        sheet.write(0, i, col[i])
    for i in range(len(datalist)):
        print("正在保存第%d条电影信息" % (i + 1))
        for j in range(4):
            sheet.write(i + 1, j, datalist[i][j])
    book.save(savepath)
    print("保存完成")


if __name__ == "__main__":
    main()
