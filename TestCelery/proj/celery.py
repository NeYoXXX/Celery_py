from celery import Celery

# 创建celery实例
app = Celery('demo')
app.config_from_object('proj.celeryconfig')

# 自动搜索任务
app.autodiscover_tasks(['proj'])