# -*- coding:utf8 -*-

import importlib, sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
importlib.reload(sys)

def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)

def download(index, title, url):
    print('download url is', url)

    name = title + '.mp4'
    # tmp_path = local + str(index)
    tmp_path = cur_file_dir()
    print('current path is-->', tmp_path)
    tmp_path = tmp_path + u"/视频/" + str(index)
    print('local path is-->', tmp_path)
    print('download method-->tmp_path is', tmp_path)

    if os.path.exists(tmp_path) == False:
        # os.mkdir(tmp_path)
        os.makedirs(tmp_path)
    local_path = os.path.join(tmp_path, name)
    print('download method--->local_path is---->', local_path)

    f = urllib.request.urlopen(url)
    with open(local_path, "wb") as code:
        code.write(f.read())


def get_load_html(url):
    # browser = webdriver.PhantomJS(executable_path='D:\software\preinstall\DevelopTool\python\module\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    # browser.get(url)
    # time.sleep(3)
    # html = browser.execute_script("return document.documentElement.outerHTML")

    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = 'C:\\Users\\Jaylee\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html


    """
    span_list = soup.find_all("span", attrs={"class": "arrow"})  # li list
    with open('home.html', 'r', 1024, "utf8") as f:
        file_content = f.read()  # read all content of file

    # if file_content != None:
    #     span_list = file_content.find_all("span", attrs={"class": "arrow"})  # li list

    for i in range(1, len(span_list)):
        if (span_list[i].find("a") is None or ""):
            continue
        else:
            data_list.append(span_list[i].find("a").get("href"))
    # pattern = '\d+'
    final_list = []
    for i in range(1, len(data_list)):
        match = re.search(pattern='\d+', string=i)
        if (match is not None):
            final_list.append(int(match))

    final_list.sort(reverse=True)
    retult = None
    if len(final_list) > 0:
        result = final_list[0]
    """