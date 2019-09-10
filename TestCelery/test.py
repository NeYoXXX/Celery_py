
'''
#  group案例
from proj.tasks import my_task1
from proj.tasks import my_task2
from proj.tasks import my_task3
from celery import group

# 将多个signature放入同一组中
my_group = group((my_task1.s(10, 10), my_task2.s(20, 20), my_task3.s(30, 30)))
ret = my_group() # 执行组任务
print(ret.get())  # 输出每个任务结果
'''
'''
# chain案例
from proj.tasks import my_task1
from proj.tasks import my_task2
from proj.tasks import my_task3
from celery import chain

# 将多个signature组成一个任务链
# my_task1的运行结果将会传递给my_task2
# my_task2的运行结果会传递给my_task3
my_chain = chain(my_task1.s(10, 10) | my_task2.s(20) | my_task3.s(30))
ret = my_chain()  # 执行任务链
print(ret.get())  # 输出最终结果
'''

from proj.tasks import *

my_task5.delay() 
my_task6.delay() 