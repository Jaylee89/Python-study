# -*- coding:utf8 -*-
import re

f = None
html = None
try:
    f = open('./2.html', 'r')
    #html = f.read()
    #print html
except IOError, e:
    print 'have an IOError', e
finally:
    if f:
        f.close()

#if html is not None:
html = '''<div class="j-r-list-c">
    <!--因为头像单独占位 所以内容需要 移动 一个头像高度 30px+间距10px -->
    <!--描述 段子 直接 只有它-->
    <div class="j-r-list-c-desc">
        <a href="/detail-24934826.html">这家理发店好，剪发顺便还把病看好了！！</a>
    </div>
    <!--视频 -->
    <div class="j-video-c"
         data-id="24934826"
         data-title="这家理发店好，..."
         data-date="2017-05-12"
         data-time="23:37"
         data-videoMlen="1.0分钟">
        <div class=" j-video" id="j-v-24934826"
             data-id="24934826"
             data-poster="http://mpic.spriteapp.cn/crop/566x360/picture/2017/0511/59145bfe30f63__b.jpg"
             data-mp4="http://mvideo.spriteapp.cn/video/2017/0511/59145bfe41056_wpcco.mp4">
        </div>


            <!--弹出推荐-->
            <div class="j-v-d-c" id="j-v-container-24934826" style="display: none;">
                <div class="video-c-dialog slideBox">
                    <div class="bd">
                        <ul>
                            <!-- 视频第一屏 -->
                            <li class="bd-1">
                                <div class="bd-1-c">
                                    <div class="bd-1-c-left">
                                        <div class="n-title">
                                            <h2 class="u-tt">扫码&nbsp;&nbsp;下载百思不得姐</h2>
                                        </div>
                                        <div class="d-qr">
                                            <i class="icon-v-d-qr"></i>
                                        </div>
                                    </div>
                                    <!-- TODO: recommend = recommend_list[forloop.counter] -->
                                    <div class="bd-1-c-right">
                                        <div class="m-list4">
                                            <ul>
                                                <li>
                                                    <div class="u-img">

                                                        <!-- 推荐的链接-->
                                                        <a href="/detail-24638180.html "
                                                           data-title=" 厉害了，我的哥..."
                                                           data-id="24638180"
                                                           data-date="2017-05-12"
                                                           data-time="23:37"
                                                           class="m-list-v-play-c" style="display: block;">
                                                            <i class="icon_play_left icon-play"></i>
                                                            <!-- gaga 图片地址 152x93 -->
                                                            <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                 class="lazy"
                                                                 data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0418/394967ba-2412-11e7-a126-1866daeb0df1_wpd.jpg"
                                                                 alt="厉害了，我的哥..."
                                                                 title="厉害了，我的哥...">
                                                        </a>
                                                    </div>
                                                    <p>&nbsp;<a href="/detail-24638180.html">
                                                        厉害了，我的哥...</a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <div class="u-img">
                                                        <!-- 推荐的链接-->
                                                        <a href="/detail-24922536.html"
                                                           data-title=" 当鳄鱼遇上猫，..."
                                                           data-id="24922536"
                                                           data-date="2017-05-12"
                                                           data-time="23:37"
                                                           class="m-list-v-play-c" style="display: block;">
                                                            <i class="icon_play_left icon-play"></i>
                                                            <!-- gaga 图片地址 152x93 -->
                                                            <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                 class="lazy"
                                                                 data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0510/24922536_487.jpg"
                                                                 alt="当鳄鱼遇上猫，...">
                                                        </a>
                                                    </div>
                                                    <p>&nbsp;<a href="/detail-24922536.html">
                                                        当鳄鱼遇上猫，...</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </li>
                            <!-- 视频第二屏 -->
                            <li class="bd-2">
                                <div class="bd-2-c">
                                    <div class="n-title n-title-down">
                                        <h2 class="u-tt u-tt-sm">
                                            <a class="v-d-hd-download btnSmXz1" href="javascript:void(0);">扫码&nbsp;&nbsp;下载百思不得姐</a>
                                        </h2>
                                    </div>
                                    <!-- 更多 -->
                                    <div class="m-list4">
                                        <ul class="bd-2-ul">


                                                    <li>
                                                        <div class="u-img ">
                                                            <!--推荐的链接-->
                                                            <a href="/detail-24671604.html"
                                                               data-title=" 《同学的名义》..."
                                                               data-id="24671604"
                                                               data-date="2017-05-12"
                                                               data-time="23:37"
                                                               class="m-list-v-play-c" style="display: block;">
                                                                <i class="icon_play_left icon-play"></i>
                                                                <!--图片地址-->
                                                                <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                     class="lazy"
                                                                     data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0421/58f9847ff13bc_wpd_16.jpg"
                                                                     alt="《同学的名义》...">
                                                            </a>
                                                        </div>
                                                        <p>&nbsp;<a href="/detail-24671604.html">
                                                            《同学的名义》...</a>
                                                        </p>
                                                    </li>

                                                    <li>
                                                        <div class="u-img ">
                                                            <!--推荐的链接-->
                                                            <a href="/detail-24772398.html"
                                                               data-title=" 我估计对面那两..."
                                                               data-id="24772398"
                                                               data-date="2017-05-12"
                                                               data-time="23:37"
                                                               class="m-list-v-play-c" style="display: block;">
                                                                <i class="icon_play_left icon-play"></i>
                                                                <!--图片地址-->
                                                                <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                     class="lazy"
                                                                     data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0429/590487344cebd__b.jpg"
                                                                     alt="我估计对面那两...">
                                                            </a>
                                                        </div>
                                                        <p>&nbsp;<a href="/detail-24772398.html">
                                                            我估计对面那两...</a>
                                                        </p>
                                                    </li>

                                                    <li>
                                                        <div class="u-img ">
                                                            <!--推荐的链接-->
                                                            <a href="/detail-24676397.html"
                                                               data-title=" 大型鸭场招鸭是..."
                                                               data-id="24676397"
                                                               data-date="2017-05-12"
                                                               data-time="23:37"
                                                               class="m-list-v-play-c" style="display: block;">
                                                                <i class="icon_play_left icon-play"></i>
                                                                <!--图片地址-->
                                                                <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                     class="lazy"
                                                                     data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0421/24676397_218.jpg"
                                                                     alt="大型鸭场招鸭是...">
                                                            </a>
                                                        </div>
                                                        <p>&nbsp;<a href="/detail-24676397.html">
                                                            大型鸭场招鸭是...</a>
                                                        </p>
                                                    </li>

                                                    <li>
                                                        <div class="u-img ">
                                                            <!--推荐的链接-->
                                                            <a href="/detail-24871292.html"
                                                               data-title=" 王者荣耀史上最..."
                                                               data-id="24871292"
                                                               data-date="2017-05-12"
                                                               data-time="23:37"
                                                               class="m-list-v-play-c" style="display: block;">
                                                                <i class="icon_play_left icon-play"></i>
                                                                <!--图片地址-->
                                                                <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                     class="lazy"
                                                                     data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0506/b6298eee-3250-11e7-b0e1-1866daeb0df1_wpd.jpg"
                                                                     alt="王者荣耀史上最...">
                                                            </a>
                                                        </div>
                                                        <p>&nbsp;<a href="/detail-24871292.html">
                                                            王者荣耀史上最...</a>
                                                        </p>
                                                    </li>


                                        </ul>
                                    </div>
                                </div>
                            </li>
                            <!-- 视频第三屏 -->
                            <li class="bd-2">
                                <div class="bd-2-c">
                                    <div class="n-title  n-title-down">
                                        <h2 class="u-tt u-tt-sm">
                                            <a class="v-d-hd-download btnSmXz2" href="javascript:void(0);">扫码&nbsp;&nbsp;下载百思不得姐</a>
                                        </h2>
                                    </div>
                                    <!-- 更多 -->
                                    <div class="m-list4">
                                        <ul class="bd-2-ul">


                                                    <li>
                                                        <div class="u-img ">
                                                            <!--推荐的链接-->
                                                            <a href="/detail-24793886.html"
                                                               data-title=" 再见六点半腿腿"
                                                               data-id="24793886"
                                                               data-date="2017-05-12"
                                                               data-time="23:37"
                                                               class="m-list-v-play-c" style="display: block;">
                                                                <i class="icon_play_left icon-play"
                                                                  ></i>
                                                                <!--图片地址-->
                                                                <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                     class="lazy"
                                                                     data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0501/24793886_127.jpg"
                                                                     alt="再见六点半腿腿">
                                                            </a>
                                                        </div>
                                                        <p>&nbsp;<a href="/detail-24793886.html">
                                                            再见六点半腿腿</a>
                                                        </p>
                                                    </li>

                                                    <li>
                                                        <div class="u-img ">
                                                            <!--推荐的链接-->
                                                            <a href="/detail-24671470.html"
                                                               data-title=" 扎心啊 老铁，..."
                                                               data-id="24671470"
                                                               data-date="2017-05-12"
                                                               data-time="23:37"
                                                               class="m-list-v-play-c" style="display: block;">
                                                                <i class="icon_play_left icon-play"
                                                                  ></i>
                                                                <!--图片地址-->
                                                                <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                     class="lazy"
                                                                     data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0421/58f980bb5794b_wpd.jpg"
                                                                     alt="扎心啊 老铁，...">
                                                            </a>
                                                        </div>
                                                        <p>&nbsp;<a href="/detail-24671470.html">
                                                            扎心啊 老铁，...</a>
                                                        </p>
                                                    </li>

                                                    <li>
                                                        <div class="u-img ">
                                                            <!--推荐的链接-->
                                                            <a href="/detail-24704896.html"
                                                               data-title=" 乔杉修睿相遇同..."
                                                               data-id="24704896"
                                                               data-date="2017-05-12"
                                                               data-time="23:37"
                                                               class="m-list-v-play-c" style="display: block;">
                                                                <i class="icon_play_left icon-play"
                                                                  ></i>
                                                                <!--图片地址-->
                                                                <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                     class="lazy"
                                                                     data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0424/58fd40622c34a_wpd_33_30.jpg"
                                                                     alt="乔杉修睿相遇同...">
                                                            </a>
                                                        </div>
                                                        <p>&nbsp;<a href="/detail-24704896.html">
                                                            乔杉修睿相遇同...</a>
                                                        </p>
                                                    </li>

                                                    <li>
                                                        <div class="u-img ">
                                                            <!--推荐的链接-->
                                                            <a href="/detail-24678368.html"
                                                               data-title=" 给大家分享一个..."
                                                               data-id="24678368"
                                                               data-date="2017-05-12"
                                                               data-time="23:37"
                                                               class="m-list-v-play-c" style="display: block;">
                                                                <i class="icon_play_left icon-play"
                                                                  ></i>
                                                                <!--图片地址-->
                                                                <img src="http://mstatic.spriteapp.cn/xx/1/w3/img/lazyload/default140.jpg"
                                                                     class="lazy"
                                                                     data-original="http://mpic.spriteapp.cn/crop/152x93/picture/2017/0421/2c8801f0-269f-11e7-81ab-1866daeb0df1_wpd.jpg"
                                                                     alt="给大家分享一个...">
                                                            </a>
                                                        </div>
                                                        <p>&nbsp;<a href="/detail-24678368.html">
                                                            给大家分享一个...</a>
                                                        </p>
                                                    </li>


                                        </ul>
                                    </div>
                                </div>
                            </li>
                        </ul>
                        <span class="icon-replay"></span>
                    </div>

                    <!-- 下面是前/后按钮代码，如果不需要删除即可 -->
                    <a class="prev" href="javascript:void(0)">
                        <i class="icon-next-arrow"></i>
                    </a>
                    <a class="next" href="javascript:void(0)">
                        <i class="icon-prev-arrow"></i>
                    </a>
                </div>
            </div>

    </div>
</div>
<div>test</div>
'''
r'''
re 所定义的 flag 包括：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为’ . ’并且包括换行符在内的任意字符（’ . ’不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和’ # ’后面的注释'''

#url_content = re.compile(r'<div class="j-r-list-c">(.*?)</div>')
url_content = re.compile(r'<div class="j-r-list-c">.*?</\w.*', re.S)
url_contents = re.findall(url_content, html)
#print url_contents
print len(url_contents)

reg = r' data-mp4="(.*?.mp4)"'
mpl_url = re.findall(reg, url_contents[0].encode('utf-8'))
print 'mpl_url is ', mpl_url