模块名称 MODULE NAME
====================

::

    timer_tool

简介 DESCRIPTION
================

::

    A Python timer module, containing class Timer() and decorator function timer(), 
    as well as some useful functions that can be used for performance analysis.
    一个Python计时器模块, 其中包含Timer()类和timer()装饰器, 以及一些有用的相关函数, 可用于程序性能分析。

包含的函数和类 Functions & Classes:
===================================

类:

class Timer
"""""""""""
    一个计时器类。A timer class.
    
    start()
        开始计时。此方法在Timer类初始化时会被自动调用。
		Start timing. This method will be automatically called when the Timer class is initialized.
    
    gettime()
        获取从计时开始到现在的时间。
		Get the elapsed time since the timer started.
    
    printtime(fmt_str="用时:{:.8f}秒")
        打印出从计时开始到现在的时间, 也就是gettime()获取的值。
		Print the time elapsed since the timer started, which is the value obtained from gettime().

函数: 

timer(msg=None, file=sys.stdout, flush=False)::

    一个装饰器, 为某个函数或生成器计时 (比使用Timer类更简洁)。
	A wrapper for timing a function or a generator that is briefer than the Timer class.
    用法:@timer(msg="用时:{time}秒")
    def func(args):
        print("Hello World!")
    
    #或:
    @timer
    def func(args):
        print("Hello World!")

示例代码 EXAMPLES
=================

示例1:

.. code-block:: python

    import timer_tool
    t=timer.Timer() #初始化Timer对象
    do_something()
    t.printtime() #输出执行do_something()所用时间 (也可使用t.gettime()获取所用时间)

示例2:

.. code-block:: python

    #退出with语句时自动打印出所用时间。
    import timer_tool
    with timer.Timer(): #在这里开始计时
        do_something()

示例3:

.. code-block:: python

    # 为某个函数计时
    from timer_tool import timer
    @timer
    def func():
        print("Hello World!")

示例4:

.. code-block:: python

    # 程序精确地延迟一段时间
    from time import sleep
    from timer_tool import sleep as sleep2
    sleep(0.0001)
    sleep2(0.0001)
    # 经测试表明, time模块的sleep()函数与本模块的函数相比, 有明显的延迟

版本 VERSION
============

    1.2.4

作者 AUTHOR
===========

    qfcy (七分诚意) qq:3076711200

    作者CSDN主页: https://blog.csdn.net/qfcy\_