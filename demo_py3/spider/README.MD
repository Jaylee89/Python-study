## Spider

### Prepare Python3 env

#### https://blog.csdn.net/xgf415/article/details/56481408/
1. Download latest source code
    - [Gzipped source tarball](https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz)
    - wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
2. Uninstall package
    - tar -xvzf  Python-3.7.1.tgz
    - cd Python-3.7.1
3. Configure and install for python new env
    - ./configure --enable-optimizations --prefix=/usr/python3
    - make && make install
    - if get error(zipimport.ZipImportError: can't decompress data; zlib not available), then run `yum -y install zlib*`
    - if get error(`ModuleNotFoundError: No module named '_ctypes'`), then run `yum -y install libffi-devel` [_ctypes](https://blog.csdn.net/qq_36416904/article/details/79316972)
4. Add soft link for python3
    - ll /usr/bin/python
    - ln -s /usr/python3/bin/python3 /usr/bin/python3
5. Test python3
    - python3 -v
    
#### bootstrap setup
0. [Reference page](https://www.cnblogs.com/LittleMore/p/6693154.html)
1. python3 app.py
2. chmod -R 777 main.sh
3. /etc/crontab
0 3 * * * root /usr/local/main.sh
4. service crond restart