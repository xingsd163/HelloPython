import logging


# logging.basicConfig()函数说明
# 该方法用于为logging日志系统做一些基本配置.

FORMAT = '%(asctime)s %(clientip)s %(user)s %(message)s'
logging.basicConfig(format=FORMAT)
d={'clientip':'192.168.1.5', 'user':'nathan'}
logger = logging.getLogger('tcpserver')
logging.warning('Protocol problem: %s', 'connection reset', extra=d)

