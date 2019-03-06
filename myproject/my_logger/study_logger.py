# coding=utf-8
import logging


def test_console_logger():
    # 设置输出info， debug信息将不过输出
    #                                                 日期占位符    名称       级别            信息
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 输出debug信息
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    logger = logging.getLogger(__name__)

    logger.info("logger.log")
    logger.debug('debug')
    logger.warning('logger.warn')


def write_log_to_file():
    # 定义日志对象
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    # 定义日志handler
    handler = logging.FileHandler('log.txt')
    handler.setLevel(level=logging.INFO)
    # 设置日志格式
    formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.info('this is a info')
    logger.warning('this is warning')
    logger.info('the end of test')


if __name__ == '__main__':
    write_log_to_file()
