# -*- coding:utf8 -*-

import hashlib

local_directory = "C:\Users\Jaylee\Desktop\cert"
list_arr = [
    "www.homeandaway.hsbc.com",
    "www.hsbcamanah.com.my",
    "www.hsbcpremier.com"
]
cert_file = [
    "interdate.cer",
    "root.cer",
    "server.cer"
]
final_result = []
def md5(filename):
    print "file path is", filename + "\n"
    with open(filename, 'r') as f:
        file_content = f.read() #read all content of file
        sha512 = hashlib.sha512()
        sha512.update(file_content)
        result = sha512.hexdigest()
        print result
        final_result.append(filename + "\t\t" + result)

def saveFile(content, filename):
    f = open(filename,"a")
    print u"正在写入文件",filename
    f.write(content.encode('utf-8'))
    f.close()

if __name__ == "__main__":

    """/*
    for fqdn in list_arr:
        temp = local_directory + "\\" + fqdn
        for _f in cert_file:
            if 
    */"""

    for fqdn in list_arr:
        temp = local_directory + "\\" + fqdn
        for _f in cert_file:
            filename = temp + "\\" + _f
            md5(filename)

    for _x in final_result:
        saveFile(_x, ".\\result.txt")
        saveFile("\n\n", ".\\result.txt")

    print u"download complete"








