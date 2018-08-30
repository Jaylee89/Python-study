#coding=utf-8
import os
import urllib
from selenium import webdriver          
from selenium.webdriver.common.keys import Keys          


#Open PhantomJS      
#driver = webdriver.PhantomJS(executable_path="phantomjs-1.9.1-windows\phantomjs.exe")
#firefoxdriver = "C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe"

firefoxdriver = r"C:\Program Files (x86)\Mozilla Firefox"
#os.environ["webdriver.gecko.driver"] = firefoxdriver
driver = webdriver.Firefox(firefoxdriver)

#myweb="192.168.1.6"
#myport="8080"

#profile=webdriver.FirefoxProfile()
#设置代理
#profile.set_preference("network.proxy.type", 1)
#profile.set_preference("network.proxy.http", myweb)
#profile.set_preference("network.proxy.http_port", myport)
#设置文件下载目录
#profile.set_preference("browser.download.folderList", 2)
#profile.set_preference("browser.download.dir", r"C:\Users\Jaylee\Desktop")
#driver=webdriver.Firefox(profile)



#访问url
driver.get(r"https://www.baidu.com/")    

print u'URL:'
print driver.current_url  
#当前链接: https://www.baidu.com/  

print u'标题:'
print driver.title  
#标题: 百度一下， 你就知道  
  
#print driver.page_source
#源代码

#定位元素，注意u1（数字1）和ul（字母L）区别
print u'\n\n定位元素id:'
info1 = driver.find_element_by_id("u1").text
print info1


#定位元素
print u'\n\n定位元素xpath:'
info3 = driver.find_element_by_xpath("//div[@id='u1']/a")
print info3.text


