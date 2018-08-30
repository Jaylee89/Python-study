#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyecharts import Pie

attr = ["男", "女", "其它"]
va = ["%.2f%%" % 56.08, "%.2f%%" % 35.81, "%.2f%%" % 8.11]
pie = Pie("男女比例分配")
pie.add("", attr, va, is_label_show = True)
pie.render()