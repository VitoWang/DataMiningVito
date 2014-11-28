#coding:utf-8
from sgmllib import SGMLParser
import sys,urllib2,urllib,cookielib

"""
denglurenrenwangbingzhuaquxinxianshi
登录人人网并抓取新鲜事
"""

class spider(SGMLParser):
    def __init__(self,email,password):
        SGMLParser.__init__(self)
        self.h3=False
        self.h3_is_ready=False
        self.div=False
        self.h3_and_div=False
        self.a=False
        self.depth=0
        self.names=""
        self.dic={}
        self.email=email
        self.password=password
        self.domian='renren.com'
        try:
            cookie=cookielib.CookieJar()
            cookieProc=urllib2.HTTPCookieProcessor(cookie)
        except:
            raise
        else:
            opener=urllib2.build_opener(cookieProc)
            urllib2.install_opener(opener)
            
    def login(self):
        url='http://www.renren.com/PLogin.do'
        postdata={
                  'email':self.email,
                  'password':self.password,
                  'domian':self.domian
                  }
        req=urllib2.Request(url,urllib.urlencode(postdata))
        self.file=urllib2.urlopen(req).read()
        #print self.file
    
    def start_h3(self,attrs):
        self.h3=True
        
    def end_h3(self):
        self.h3=False
        self.h3_is_ready=True
        
    def start_a(self,attrs):
        if self.h3 or self.div:
            self.a=True
            
    def end_a(self):
        self.a=False
        
    def start_div(self,attrs):
        if not self.h3_is_ready:
            return
        if self.div:
            self.depth += 1
        for k,v in attrs:
            if k == 'class' and v == 'content':
                self.div=True
                self.h3_and_div=True    #h3 and div is connected
                
    def end_div(self):
        if self.depth==0:
            self.div=False
            self.h3_and_div=False
            self.h3_is_ready=False
            self.names=""
        if self.div:
            self.depth -= 1
            
    def handle_data(self,text):
        #record the name
        if self.h3 and self.a:
            self.names += text
        #record says
        if self.h3 and (not self.a):
            if not text:pass
            else:
                self.dic.setdefault(self.names,[]).append(text)
                return
        if self.h3_and_div:
            self.dic.setdefault(self.names,[]).append(text)
            
    def show(self):
        type=sys.getfilesystemencoding()
        for key in self.dic:
            s1=((''.join(key)).replace(' ','')).decode('utf-8').encode(type)
            s2=((''.join(self.dic[key])).replace(' ', '')).decode('utf-8').encode(type)
            print s1,s2
            
            

#renrenspider=spider('929431626@qq.com','wang4502')
#renrenspider.login()
#renrenspider.feed(renrenspider.file)
#renrenspider.show()