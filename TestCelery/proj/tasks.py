from proj.celery import app as celery_app

# 创建任务函数
@celery_app.task
def my_task1(a , b):
    print("任务函数(my_task1)正在执行....")
    return a+b

@celery_app.task
def my_task2(a,b):
    print("任务函数(my_task2)正在执行....")
    return a+b

@celery_app.task
def my_task3(a,b):
    print("任务函数(my_task3)正在执行....")
    return a+b

@celery_app.task
def my_task5():
    print("任务函数(my_task5)正在执行....")

@celery_app.task
def my_task6():
    print("任务函数(my_task6)正在执行....")

@celery_app.task
def my_task7():
    print("任务函数(my_task7)正在执行....")

# 周期执行任务
@celery_app.task
def my_task8():
    print("任务函数(my_task8)正在执行....")

    