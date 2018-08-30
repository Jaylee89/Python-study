#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, sys, os, re, time
from optparse import OptionParser

class wget:
    def __init__(self, config = {}):
        self.config = {
            'block': int(config['block'] if config.has_key('block') else 1024),
        }
        self.total = 0
        self.size = 0
        self.filename = ''

    def touch(self, filename):
        with open(filename, 'w') as fin:
            pass

    def remove_nonchars(self, name):
        (name, _) = re.subn(ur'[\\\/\:\*\?\"\<\>\|]', '', name)
        return name

    def support_continue(self, url):
        headers = {
            'Range': 'bytes=0-4'
        }
        try:
            r = requests.head(url, headers = headers)
            crange = r.headers['content-range']
            self.total = int(re.match(ur'^bytes 0-4/(\d+)$', crange).group(1))
            return True
        except:
            pass
        try:
            self.total = int(r.headers['content-length'])
        except:
            self.total = 0
        return False

    def download(self, url, filename, headers = {}):
        finished = False
        block = self.config['block']
        local_filename = self.remove_nonchars(filename)
        tmp_filename = local_filename + '.downtmp'
        size = self.size
        total = self.total
        if self.support_continue(url):  # 支持断点续传
            try:
                with open(tmp_filename, 'rb') as fin:
                    self.size = int(fin.read())
                    size = self.size + 1
            except:
                self.touch(tmp_filename)
            finally:
                headers['Range'] = "bytes=%d-" % (self.size, )
        else:
            self.touch(tmp_filename)
            self.touch(local_filename)
        r = requests.get(url, stream = True, verify = False, headers = headers)
        if r.status_code != 200:
            print "[+] have issue, status_code is %d" % r.status_code
            sys.exit()
        if total > 0:
            print "[+] Size: %dKB" % (total / 1024)
        else:
            print "[+] Size: None"
        start_t = time.time()
        with open(local_filename, 'ab+') as f:
            f.seek(self.size)
            f.truncate()
            try:
                for chunk in r.iter_content(chunk_size = block): 
                    if chunk:
                        f.write(chunk)
                        size += len(chunk)
                        f.flush()
                    sys.stdout.write('\b' * 64 + 'Now: %d, Total: %s' % (size, total))
                    sys.stdout.flush()
                finished = True
                os.remove(tmp_filename)
                spend = int(time.time() - start_t)
                speed = int((size - self.size) / 1024 / spend)
                sys.stdout.write('\nDownload Finished!\nTotal Time: %ss, Download Speed: %sk/s\n' % (spend, speed))
                sys.stdout.flush()
                print 'is finished, ', finished
            except:
                import traceback
                print traceback.print_exc()
                print "\nDownload pause.\n"
            finally:
                if not finished:
                    with open(tmp_filename, 'wb') as ftmp:
                        ftmp.write(str(size))

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url",  
                      help="target url")
    parser.add_option("-o", "--output", dest="filename",  
                      help="download file to save")
    #parser.add_option("-a", "--user-agent", dest="useragent", 
    #                  help="request user agent", default='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 \
    #                  (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')
    parser.add_option("-a", "--user-agent", dest="useragent", 
                      help="request user agent", default='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
                      (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345 Explorer/8.4.1.14855')
    
    parser.add_option("-r", "--referer", dest="referer", 
                      help="request referer")
    parser.add_option("-c", "--cookie", dest="cookie", 
                      help="request cookie", default = 'foo=1;')
    (options, args) = parser.parse_args()
    if not options.url:
        print 'Missing url'
        sys.exit()
    if not options.filename:
        options.filename = options.url.split('/')[-1]
    headers = {
        'User-Agent': options.useragent,
        'Referer': options.referer if options.referer else options.url,
        'Cookie': options.cookie
    }
    print 'url is', options.url
    print 'filename is', options.filename
    wget().download(options.url, options.filename)


#command as below
#python file_download.py --url "https://mule-studio.s3.amazonaws.com/6.2.2-U2/AnypointStudio-for-win-64bit-6.2.2-201701271427.zip"

#python file_download.py --url "https://assets-cdn.github.com/pinned-octocat.svg"
#python file_download.py --url "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1491417924865&di=c2d5afc5ba38f371f8486af95ff54d8d&imgtype=0&src=http%3A%2F%2Fi1.ce.cn%2Fce%2Fcelt%2Fwyry%2F201305%2F06%2FW020130506329671709790.jpg"
#python file_download.py --url https://unpkg.com/vue/dist/vue.js
#python file_download.py --url http://192.168.1.2:30001/GTLCP.apk
#python file_download.py --url http://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz
#python file_download.py --url http://mirrors.163.com/centos/7.3.1611/isos/x86_64/CentOS-7-x86_64-LiveGNOME-1611.iso
#python file_download.py --url http://ec2-34-228-202-18.compute-1.amazonaws.com/find/f7521f2d4f1ed7d417e7060a9974e8ad/result-388991450.dl?source=direct&return_url=http%3A%2F%2Fdownload-new.utorrent.com%2Fendpoint%2Futorrent%2Fos%2Fwindows%2Ftrack%2Fstable%2F
#文件下载，需要处理https的问题

#python file_download.py --url http://download.plugins.jetbrains.com/6954/28546/kotlin-plugin-1.0.4-release-IJ143-115.zip?updateId=28546&pluginId=6954&uuid=5bc8fde9-9208-423d-86e8-0eeb9242bccf&code=IU&build=143.2287

#python file_download.py --url https://pypi.python.org/packages/c3/0a/3875a23af9e6e47d447c1791b300ac36145e5ce023d739fec42885745bf3/kivy.deps.gstreamer-0.1.12-cp27-cp27m-win_amd64.whl#md5=2ac42d6fe96970a058ecdc257a50363c