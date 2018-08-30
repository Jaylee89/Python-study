#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''


http://www.pygame.org/news


'''


import pygame
print pygame.ver

使用Pygame

Pygame有很多的模块，下面是一张一览表：
模块名          功能
pygame.cdrom    访问光驱
pygame.cursors  加载光标
pygame.display  访问显示设备
pygame.draw     绘制形状、线和点
pygame.event    管理事件
pygame.font     使用字体
pygame.image    加载和存储图片
pygame.joystick 使用游戏手柄或者 类似的东西
pygame.key      读取键盘按键
pygame.mixer    声音
pygame.mouse    鼠标
pygame.movie    播放视频
pygame.music    播放音频
pygame.overlay  访问高级视频叠加
pygame          
pygame.rect     管理矩形区域
pygame.sndarray 操作声音数据
pygame.sprite   操作移动图像
pygame.surface  管理图像和屏幕
pygame.surfarray管理点阵图像数据
pygame.time     管理时间和帧信息
pygame.transform缩放和移动图像


事件
Pygame的做法是把一系列的事件存放一个队列里，逐个的处理

事件检索

pygame.event.get()来处理所有的事件，这好像打开大门让所有的人进入。
如果我们使用pygame.event.wait()，Pygame就会等到发生一个事件才继续下去，
pygame.event.poll()一旦调用，它会根据现在的情形返回一个真实的事件，或者一个“什么都没有”。

下表是一个常用事件集：
事件            产生途径                       参数
QUIT            用户按下关闭按钮               none
ATIVEEVENT      Pygame被激活或者隐藏           gain, state
KEYDOWN         键盘被按下                     unicode, key, mod
KEYUP           键盘被放开                     key, mod
MOUSEMOTION     鼠标移动                       pos, rel, buttons
MOUSEBUTTONDOWN 鼠标按下                       pos, button
MOUSEBUTTONUP   鼠标放开                       pos, button
JOYAXISMOTION   游戏手柄(Joystick or pad)移动  joy, axis, value
JOYBALLMOTION   游戏球(Joy ball)?移动          joy, axis, value
JOYHATMOTION    游戏手柄(Joystick)?移动        joy, axis, value
JOYBUTTONDOWN   游戏手柄按下                   joy, button
JOYBUTTONUP     游戏手柄放开                   joy, button
VIDEORESIZE     Pygame窗口缩放                 size, w, h
VIDEOEXPOSE     Pygame窗口部分公开(expose)     none
USEREVENT       触发了一个用户事件             code



处理鼠标事件

MOUSEMOTION事件会在鼠标动作的时候发生，它有三个参数：
buttons – 一个含有三个数字的元组，三个值分别代表左键、中键和右键，1就是按下。
pos     – 位置
rel     – 代表了现在距离上次产生鼠标事件时的距离

和MOUSEMOTION类似的，我们还有MOUSEBUTTONDOWN和MOUSEBUTTONUP两个事件，看名字就明白是什么意思了。很多时候，
你只需要知道鼠标点下就可以了，那就可以不用上面那个比较强大（也比较复杂）的事件。它们的参数为：
button – 对应按键的值
pos    – 位置

处理键盘事件

KEYDOWN和KEYUP的参数描述如下：
key – 按下或者放开的键值，是一个数字，Pygame中你可以使用K_xxx来表示，比如字母a就是K_a，还有K_SPACE和K_RETURN等。
mod – 包含了组合键信息，如果mod & KMOD_CTRL是真的话，表示用户同时按下了Ctrl键。类似的还有KMOD_SHIFT，KMOD_ALT。
unicode – 代表了按下键的Unicode值

事件过滤

使用pygame.event.set_blocked(事件名)来完成。
如果有好多事件需要过滤，可以传递一个列表，比如pygame.event.set_blocked([KEYDOWN, KEYUP])，
如果设置参数None，那么所有的事件有被打开了。
使用pygame.event.set_allowed()来设定允许的事件。


产生事件 (录像/事件回放)

通常玩家做什么，Pygame就产生对应的事件就可以了，
不过有的时候我们需要模拟出一些事件来，比如录像回放的时候，我们就要把用户的操作再现一遍。

my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u' ')
#你也可以像下面这样写，看起来比较清晰（但字变多了……）
my_event = pygame.event.Event(KEYDOWN, {"key":K_SPACE, "mod":0, "unicode":u' '})
pygame.event.post(my_event)

CATONKEYBOARD = USEREVENT+1
my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
pgame.event.post(my_event)
 
#然后获得它
for event in pygame.event.get():
    if event.type == CATONKEYBOARD:
        print event.message


全屏显示
可变尺寸的显示
其他、复合模式

我们还有一些其他的显示模式，但未必所有的操作系统都支持（放心windows、各种比较流行的Linux发行版都是没问题的），一般来说窗口就用0全屏就用FULLSCREEN，这两个总是OK的。
如果你想创建一个硬件显示（surface会存放在显存里，从而有着更高的速度），你必须和全屏一起使用：

screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | FULLSCREEN, 32)

当然你完全可以把双缓冲（更快）DOUBLEBUF也加上，这就是一个很棒的游戏显示了，不过记得你要使用pygame.display.flip()来刷新显示。pygame.display.update()是将数据画到前面显示，而这个是交替显示的意思。
稍微说一下双缓冲的意思，可以做一个比喻：我的任务就是出黑板报，如果只有一块黑板，那我得不停的写，全部写完了稍微Show一下就要擦掉重写，这样一来别人看的基本都是我在写黑板报的过程，看到的都是不完整的黑板报；如果我有两块黑板，那么可以挂一块给别人看，我自己在底下写另一块，写好了把原来的换下来换上新的，这样一来别人基本总是看到完整的内容了。双缓冲就是这样维护两个显示区域，快速的往屏幕上换内容，而不是每次都慢慢地重画。
还有OPENGL模式，这是一个得到广泛应用的3D加速显示模式。不过一旦使用了这个模式，pygame中的2D图像函数就不能用了


http://www.pythontab.com/html/2012/pythongui_1220/25.html