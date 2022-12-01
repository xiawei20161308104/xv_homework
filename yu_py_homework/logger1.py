'''
Version: 1.0
Author: xiawei
Date: 2022-10-20 12:23:29
LastEditors: xiawei
LastEditTime: 2022-10-20 12:59:06
Description: 
'''
# -*- coding: utf-8 -*-


import sys
import logging
from pathlib import Path
from logging import handlers
import os
# sys.path.append(str(Path(__file__).resolve().parents[0]))

current_directory = os.path.dirname(os.path.abspath(__file__))
# 日志级别关系映射
level_relations = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'crit': logging.CRITICAL
}


def _get_logger(filename, level='info'):
    # 创建日志对象
    log = logging.getLogger(filename)
    # 设置日志级别
    log.setLevel(level_relations.get(level))
    # 日志输出格式
    fmt = logging.Formatter(
        '%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 输出到控制台
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(fmt)
    # 输出到文件
    # 日志文件按天进行保存，每天一个日志文件
    file_handler = handlers.TimedRotatingFileHandler(
        filename=filename, when='D', backupCount=1, encoding='utf-8')
    # 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
    # file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=1*1024*1024*1024, backupCount=1, encoding='utf-8')
    file_handler.setFormatter(fmt)

    log.addHandler(console_handler)
    log.addHandler(file_handler)
    return log


# 明确指定日志输出的文件路径和日志级别
logger = _get_logger(current_directory+'/logs', 'info')
"""
demo:

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from logger1 import logger
logger.logger.info('ss')
"""
# logger.info('ss')
