#! /bin/env python
# -*- coding: utf-8 -*-
__author__ = 'anonymous_ch'
import urllib,urllib2,cookielib,re
 
 
def login_func():
    login_page = "http://www.renren.com/ajaxLogin/login"
    data = {'email': '929431626@qq.com', 'password': 'wang4502'}
    post_data = urllib.urlencode(data)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    print u"登录人人网"
    req = opener.open(login_page, post_data)
    req = urllib2.urlopen("http://www.renren.com/home")
    html = req.read()
    uid = re.search("'ruid':'(\d+)'", html).group(1)#获取用户的uid"
    print  u"登陆成功"
    return uid
 
 
def get_list(uid):
    pagenum = 0
    print u"开始解析好友列表"
    while True:
        page = "http://friend.renren.com/GetFriendList.do?curpage=" + str(pagenum) + "&id=" + str(uid)
        res = urllib2.urlopen(page)
        html = res.read()
        pattern = '<a href="http://www\.renren\.com/profile\.do\?id=(\d+)"><img src="[\S]*" alt="[\S]*[\s]\((.*)\)" />'
        m = re.findall(pattern, html)#查找目标
        if len(m) == 0:
            break#不存在
        for i in range(0, len(m)):
            userid = m[i][0]
            uname = m[i][1]
            try:
                print u"账户："+userid+u"     姓名："+unicode(uname,'utf-8')
            except:
                print u"账户："+userid+u"     姓名：",
                print uname,
                print " "
        pagenum += 1
    print u"好友列表分析完毕."
 
if __name__ =="__main__":
    get_list(login_func())