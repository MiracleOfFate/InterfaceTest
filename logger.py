import json, logging

# 创建一个日志器
logger = logging.getLogger('test')  # 实例化对象

# 设置日志输出最低等级，低于当前等级就会被忽略
logger.setLevel(logging.DEBUG)  # 输出所有大于DEBUG级别的log

# 创建一个格式器 —— 设置日志输出格式
fmt = logging.Formatter('[%(filename)-6s]:[%(levelname)-6s][%(asctime)s]:%(message)s')

# 创建一个处理器
stream_hd1 = logging.StreamHandler()  # 终端（控制台）输出

stream_hd1.setFormatter(fmt)
stream_hd1.setLevel(logging.DEBUG)
logger.addHandler(stream_hd1)

if __name__ == '__main__':
    logger.info('this is info')
