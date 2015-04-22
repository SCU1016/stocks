#!/bin/python
#-*- coding:utf-8 -*-
from urllib2 import *
from Tonghuashun import *
import sys
reload(sys)   
sys.setdefaultencoding('utf-8')   #修改默认编码方式，默认为ascci
filePath='.\\'
ob=Tonghuashun(filePath)
ob.run()
