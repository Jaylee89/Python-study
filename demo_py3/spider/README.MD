## Spider

### Prepare Python3 env

#### https://blog.csdn.net/xgf415/article/details/56481408/
1. Download latest source code
    - [Gzipped source tarball](https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz)
    - wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
2. Uninstall package
    - tar -xvzf Python-3.7.1.tgz
    - cd Python-3.7.1
3. Configure and install for python new env
    - ./configure --with-ssl --with-openssl=/usr/local/ --enable-optimizations --prefix=/usr/python3
    - vi Modules/Setup
    - SSL=/usr/local
        _ssl _ssl.c \
                -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
                -L$(SSL)/lib -lssl -lcrypto
    - make
    - make install
    - if get error(zipimport.ZipImportError: can't decompress data; zlib not available), then run `yum -y install zlib*`
    - if get error(`ModuleNotFoundError: No module named '_ctypes'`), then run `yum -y install libffi-devel` [_ctypes](https://blog.csdn.net/qq_36416904/article/details/79316972)
    - need to install `yum install openssl openssl-libs` [SSL module](https://blog.csdn.net/chief_victo/article/details/80425431)
4. Add soft link for python3
    - ll /usr/bin/python
    - ln -s /usr/python3/bin/python3 /usr/bin/python3
5. Test python3
    - python3 -v
    
#### bootstrap setup
https://www.cnblogs.com/zhengah/p/4952311.html
0. [Reference page](https://www.cnblogs.com/LittleMore/p/6693154.html)
1. python3 app.py
2. chmod -R 777 main.sh
3. /etc/crontab
0 */3 * * * root /usr/local/main.sh
4. service crond restart

#### install dependency
1. yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite sqlite-devel readline-devel tk tk-devel gdbm gdbm-devel db4-devel libpcap-devel lzma xz xz-devel libuuid-devel libffi-devel
2. [ssl issue](https://blog.csdn.net/devalone/article/details/82459276?utm_source=blogxgwz1)
3. [have issue][ignore][libressl-2.8.2.tar.gz might work, need to retry][LibreSSL version](https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/)
    - ./configure --prefix=/usr/local
    - make && make install
    - [Reference](https://blog.csdn.net/devalone/article/details/82459276?utm_source=blogxgwz1)
        - in /etc/ld.so.conf.d/local.conf, add /usr/local/lib
        - ldconfig -v (重新加载共享模块)
        - openssl version
4. [install higher version for openssl](https://blog.csdn.net/u013898698/article/details/79174029/)
    - wget http://www.openssl.org/source/openssl-1.1.1a.tar.gz
    - tar -xvzf openssl-1.1.1a.tar.gz
    - cd openssl-1.1.1a
    - ./config shared zlib --prefix=/usr/local
    - make && make install
    - in /etc/ld.so.conf.d/local.conf, add /usr/local/lib64 (libssl.so.1.1 is under lib64)
    - ldconfig -v
    - ldd /usr/local/bin/openssl
    - [sample](https://gist.github.com/JulienPalard/9424a59721a9634e84da1f5b3c699789)
    - [experience, still has issue](https://segmentfault.com/q/1010000015781670/revision) 
    - [bugs.python.org](https://bugs.python.org/issue34028)
    - [forum](https://groups.google.com/forum/#!topic/dev-python/ApNm0YH-V8g)
    
## https://www.jianshu.com/p/2a5cd519e583
 - ls -l /usr/bin | grep python
 - ln -s /usr/bin/pip3 /usr/bin/pip
 - ln -s /usr/python3/lib/python3.6/site-packages/pip /usr/bin/pip
 - ln -s /usr/lib/python2.7/site-package/pip /usr/bin/pip
 - ls -l /usr/bin | grep python
 
## dependency install
 - python3 -m pip install --upgrade XXX
 - python3 -m pip install -r requirements.txt
 - pip3 install --upgrade pip