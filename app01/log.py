#-*- coding:utf-8 -*-

import logging
import os
import datetime

class Logger(object):

    def __init__(self,logger):
        #打印日志格式
        log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
        formatter = logging.Formatter(log_fmt)
        # 设置日志文件名称以及存放路径
        log_path = os.path.dirname(os.path.abspath('.')) + '/fcy007/logs/'
        time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
        log_name = log_path+time+ '.log'
        #创建handler
        ch = logging.StreamHandler()
        fh = logging.FileHandler(log_name)
        #格式化输出
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        #创建logger实例化对象
        self.log = logging.getLogger(logger)
        self.log.setLevel(logging.INFO)
        self.log.addHandler(ch)
        self.log.addHandler(fh)

    def getlog(self):
        return self.log
