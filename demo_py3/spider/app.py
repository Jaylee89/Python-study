# -*- coding:utf8 -*-

import re, random, time, datetime
import importlib, sys, os, io
from functions.education.Education import Education

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# importlib.reload(sys)



if __name__ == "__main__":
    edu = Education(r"http://www.gzedu.gov.cn", 1)
    edu.start()

    begin = datetime.datetime.now()
    # edu = gz_education(r"http://www.gzedu.gov.cn/gzsjyj/tzgg/")
    edu = gz_education(r"http://www.gzedu.gov.cn", 1)
    public_url = edu.path_absolution()
    final_url = public_url.format("list.shtml")

    max_page = edu.getMaxPage(final_url)
    # max_page = 5
    for i in list(range(1, max_page)):
        if i is not 1:
            final_url = public_url.format("list_%d.shtml" % (i))
            break
        log.debug('final_url--->' + final_url)
        time.sleep(random.randint(0, 2))
        edu.main(i, final_url)
    end = datetime.datetime.now()
    k = end - begin
    log.debug("complete spider, usage time is %s" % k)
