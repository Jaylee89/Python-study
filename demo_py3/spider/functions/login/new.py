#-*- encoding:utf-8 -*-

import requests
import re
import base64,rsa,binascii

username = '18182428724'  #用户名
password = 'jal891012'  #密码
header={'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'152',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'',
    'Host':'passport.weibo.cnn',
    'Referer':'http://login.sina.com.cn/sso/prelogin.php',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}

def Get_cookies(username,password):
    '''登陆新浪微博，获取登陆后的Cookie，返回到变量cookies中'''
    url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.15)%'+username
    html = requests.get(url, header)
    html.encoding = 'gb2312'
    text = html.text
    servertime = re.findall('"servertime":(.*?),',text,re.S)[0]
    nonce = re.findall('"nonce":"(.*?)"',text,re.S)[0]
    pubkey = re.findall('"pubkey":"(.*?)"',text,re.S)[0]
    rsakv = re.findall('"rsakv":"(.*?)"',text,re.S)[0]

    username = base64.b64encode(username.encode('utf-8')) #加密用户名

    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
    passwd = rsa.encrypt(message.encode('utf-8'), key) #加密
    passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。

    login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.4)'
    data = {'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '30',
        'userticket': '1',
        'ssosimplelogin': '1',
        'vsnf': '1',
        'vsnval': '',
        'su': username,
        'service': 'miniblog',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'sp': passwd,
        'encoding': 'UTF-8',
        'prelt': '115',
        'rsakv' : rsakv,
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
        }
    html = requests.post(login_url,data=data)#.content
    html.encoding = 'gb2312'
    text = html.text
    urlnew = re.findall('location.replace\(\'(.*?)\'',text,re.S)[0]

    html = requests.get(urlnew)
    cookies = html.cookies
    return cookies

def get_myuid(cookies):
    # url = 'http://weibo.com/'
    # url = "http://weibo.com//%d/info" % (2608649530)
    url = "http://weibo.com/%s" % ("gzeduwb")
    html = requests.get(url,cookies=cookies) #用get请求加入cookies参数登陆微博主页
    html.encoding = 'utf-8'
    text = html.text

    a = text.find('[\'uid\']=')
    b = text[a:].find(';')
    myuid = text[a + len('[\'uid\']='): a + b][1:-1] #获取我的uid

    a = text.find('[\'nick\']=')
    b = text[a:].find(';')
    myname = text[a + len('[\'nick\']='): a + b][1:-1] #获取我的用户名
    return myuid,myname

def get_weibo(uid,cookies,page):
    '''获取我的前page页的微博'''

    url = 'http://weibo.com/'+uid+'/profile'
    my_weibo = []
    for p in range(1,page+1):

        #新浪微博每一页信息是异步加载的，分三次加载
        for pb in range(-1,2):
            data = {'pagebar':str(pb),
                    'pre_page':str(p),
                    'page':str(p),
                    }
            if p == 1:
                if pb == -1:
                    html = requests.get(url,cookies=cookies)
                    html.encoding = 'utf-8'
                    html = html.text
                else:
                    html = requests.get(url,cookies=cookies,params=data)
                    html.encoding = 'utf-8'
                    html = html.text
            else:
                html = requests.get(url,cookies=cookies,params=data)
                html.encoding = 'utf-8'
                html = html.text

            hlist = html.split('node-type=\\"feed_list_content\\"')[1:]
            for i in hlist:
                i = i.split('<\/div>')[0]
                s = re.findall('>(.*?)<',i)
                weibo = ''
                for j in s:
                    weibo = weibo + j.strip('\\n /\\')
                if len(weibo) != 0:
                    my_weibo.append(weibo)
    return my_weibo

def get_follow(myuid,cookies):

    '''获取微博关注用户的uid与用户名'''
    url = 'http://weibo.com/' + myuid + '/follow'
    html = requests.get(url,cookies=cookies)
    html.encoding = 'utf-8'
    text = html.text

    c = text.find('member_ul clearfix')-13
    text = text[c:]
    u = re.findall(r'[uid=]{4}([0-9]+)[&nick=]{6}(.*?)\\"',text)

    user_id = []
    uname = []
    for i in u:
        user_id.append(i[0]) #把uid储存到列表user_id中
        uname.append(i[1])   #把用户名储存到列表uname中
    return user_id,uname

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
cookies = Get_cookies(username,password)   #获取登陆后的cookies
myuid,myname = get_myuid(cookies)          #获取我的uid与用户名
uid,uname = get_follow(myuid,cookies)      #获取关注用户的uid与用户名

with open('user_weibo.txt', "w", 1024, "utf8") as f:
    for i in range(len(uid)):
        my_weibo = get_weibo(uid[i],cookies,3)   #获取用户前三页的微博信息
        for j in my_weibo:
            f.write(uid[i]+' '+uname[i]+' '+j+'\n')
        print(str(i+1)+'/'+str(len(uid)))

print('所有用户获取完成')