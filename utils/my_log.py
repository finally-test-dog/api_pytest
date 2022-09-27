# *coding:utf-8 *
import logging
import os.path
import time


root_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
log_path = os.path.join(root_path, "log")


class Logger:

    def __init__(self):
        # 定义日志位置和文件名
        # self.logname = os.path.join(log_path, "{}.log".format(time.strftime("%Y-%m-%d")))
        self.logname = os.path.join(log_path, "%s.log" % (time.strftime("%Y-%m-%d")))
        # 定义一个日志容器
        self.logger = logging.getLogger('log')
        # 设置日志的打印的级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输入的格式
        self.formatter = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d] - %(levelname)s : %(message)s')
        # 创建日志处理器，存放日志文件
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="utf-8")
        # 文件存放日志级别
        self.filelogger.setLevel(logging.DEBUG)
        # 文件存放日志格式
        self.filelogger.setFormatter(self.formatter)
        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()
        # 设置控制台打印级别
        self.console.setLevel(logging.DEBUG)
        # 控制台打印日志格式
        self.console.setFormatter(self.formatter)
        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == "__main__":
    logger.info('1')
    logger.error('2')
    logger.warning('3')