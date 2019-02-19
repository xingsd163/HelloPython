# # PyCharm comment shortcut: Ctrl + /
# # This is a comment test
# https://www.cnblogs.com/yyds/p/6901864.html
# 几乎所有开发语言都会内置日志相关功能，或者会有比较优秀的第三方库来提供日志操作功能，比如：log4j，log4php等。它们功能强大、使用简单。Python自身也提供了一个用于记录日志的标准库模块--logging。

# logging模块默认定义了以下几个日志等级，它允许开发人员自定义其他日志级别，但是这是不被推荐的，尤其是在开发供别人使用的库时，因为这会导致日志级别的混乱。
# DEBUG	最详细的日志信息，典型应用场景是 问题诊断
# INFO	信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
# WARNING	当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
# ERROR	由于一个更严重的问题导致某些功能不能正常运行时记录的信息
# CRITICAL	当发生严重错误，导致应用程序不能继续运行时记录的信息
# 开发应用程序或部署开发环境时，可以使用DEBUG或INFO级别的日志获取尽可能详细的日志信息来进行开发或部署调试；应用上线或部署生产环境时，应该使用WARNING或ERROR或CRITICAL级别的日志来降低机器的I/O压力和提高获取错误日志信息的效率。日志级别的指定通常都是在应用程序的配置文件中进行指定的。

# logging模块提供了两种记录日志的方式：
#
# 第一种方式是使用logging提供的模块级别的函数
# 第二种方式是使用Logging日志系统的四大组件

import logging
import logging.handlers
import datetime



#
# logging.debug("This is a debug log")
# logging.info("This is an info log")
# logging.warning("This is a warning log")
# logging.error("This is an error log")

#
# 问题1：为什么前面两条日志没有被打印出来？
# 这是因为logging模块提供的日志记录函数所使用的日志器设置的日志级别是WARNING，因此只有WARNING级别的日志记录以及大于它的ERROR和CRITICAL级别的日志记录被输出了，而小于它的DEBUG和INFO级别的日志记录被丢弃了。
#
# 问题2：打印出来的日志信息中各字段表示什么意思？为什么会这样输出？
# 上面输出结果中每行日志记录的各个字段含义分别是：
#
# 日志级别:日志器名称:日志内容
# 之所以会这样输出，是因为logging模块提供的日志记录函数所使用的日志器设置的日志格式默认是BASIC_FORMAT，其值为：
#
# "%(levelname)s:%(name)s:%(message)s"
# 问题3：如果将日志记录输出到文件中，而不是打印到控制台？
# 因为在logging模块提供的日志记录函数所使用的日志器设置的处理器所指定的日志输出位置默认为:
# sys.stderr。

# logging.basicConfig()函数说明
# 该方法用于为logging日志系统做一些基本配置.

# logging.basicConfig(level=logging.INFO)
# logging.debug("This is a debug log")
# logging.info("This is an info log")
# logging.warning("This is a warning log")
# logging.error("This is an error log")


# 配置下日志输出目标文件和日志格式
# asctime	%(asctime)s	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
# created	%(created)f	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
# levelname	%(levelname)s	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
# name	%(name)s	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
# message	%(message)s	日志记录的文本内容，通过 msg % args计算得到的

# LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
# LOG_FORMAT2="%(asctime)s, %(levelname)s, %(message)s"
# logging.basicConfig(filename="/home/nathan/my.log", level=logging.DEBUG, format=LOG_FORMAT2)
#
# logging.debug("This is a debug log")
# logging.info("This is an info log")
# logging.warning("This is a warning log")
# logging.error("This is an error log")
#
# log_file=open("/home/nathan/my.log","r")
# print(log_file.read())

# logging日志模块四大组件
# 在介绍logging模块的日志流处理流程之前，我们先来介绍下logging模块的四大组件：
#
# 组件名称	对应类名	功能描述
# 日志器	Logger	提供了应用程序可一直使用的接口
# 处理器	Handler	将logger创建的日志记录发送到合适的目的输出
# 过滤器	Filter	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
# 格式器	Formatter	决定日志记录的最终输出格式
#
# 日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；
# 不同的处理器（handler）可以将日志输出到不同的位置；
# 日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
# 每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
# 每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。
# 简单点说就是：日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。

# Logger对象最常用的方法分为两类：配置方法 和 消息发送方法
# Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
# Logger.addHandler() 和 Logger.removeHandler()	为该logger对象添加 和 移除一个handler对象
# Logger.addFilter() 和 Logger.removeFilter()	为该logger对象添加 和 移除一个filter对象

# 那么，怎样得到一个Logger对象呢？一种方式是通过Logger类的实例化方法创建一个Logger类的实例，但是我们通常都是用第二种方式--logging.getLogger()方法。
#
# Handler类
# Handler对象的作用是（基于日志消息的level）将消息分发到handler指定的位置（文件、网络、邮件等）。Logger对象可以通过addHandler()方法为自己添加0个或者更多个handler对象。比如，一个应用程序可能想要实现以下几个日志需求：
#
# 1）把所有日志都发送到一个日志文件中；
# 2）把所有严重级别大于等于error的日志发送到stdout（标准输出）；
# 3）把所有严重级别为critical的日志发送到一个email邮件地址。
# 这种场景就需要3个不同的handlers，每个handler复杂发送一个特定严重级别的日志到一个特定的位置。
# 一个handler中只有非常少数的方法是需要应用开发人员去关心的。对于使用内建handler对象的应用开发人员来说，似乎唯一相关的handler方法就是下面这几个配置方法：
#
# 方法	描述
# Handler.setLevel()	设置handler将会处理的日志消息的最低严重级别
# Handler.setFormatter()	为handler设置一个格式器对象
# Handler.addFilter() 和 Handler.removeFilter()	为handler添加 和 删除一个过滤器对象
#
# Formater类
# Formater对象用于配置日志信息的最终顺序、结构和内容。与logging.Handler基类不同的是，应用代码可以直接实例化Formatter类。另外，如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成。
#
# Formatter类的构造方法定义如下：
#
# logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
#
# Filter类
# Filter可以被Handler和Logger用来做比level更细粒度的、更复杂的过滤功能。Filter是一个过滤器基类，它只允许某个logger层级下的日志事件通过过滤。


#
# 例子
#
# 1. 需求
# 现在有以下几个日志记录的需求：
#
# 1）要求将所有级别的所有日志都写入磁盘文件中
# 2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
# 3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
# 4）要求all.log在每天凌晨进行日志切割
# 2. 分析
# 1）要记录所有级别的日志，因此日志器的有效level需要设置为最低级别--DEBUG;
# 2）日志需要被发送到两个不同的目的地，因此需要为日志器设置两个handler；另外，两个目的地都是磁盘文件，因此这两个handler都是与FileHandler相关的；
# 3）all.log要求按照时间进行日志切割，因此他需要用logging.handlers.TimedRotatingFileHandler; 而error.log没有要求日志切割，因此可以使用FileHandler;
# 4）两个日志文件的格式不同，因此需要对这两个handler分别设置格式器；
#

# import logging
# import logging.handlers
# import datetime


logger=logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

rf_handler=logging.handlers.TimedRotatingFileHandler('/home/nathan/all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0,0,0,0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler=logging.FileHandler('/home/nathan/error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug("debug messsage")
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')











