result_backend = 'redis://localhost:6379/1'
broker_url = 'redis://localhost:6379/0'

task_routes=({
    'proj.tasks.my_task5': {'queue': 'queue1'},
    'proj.tasks.my_task6': {'queue': 'queue1'},
    'proj.tasks.my_task7': {'queue': 'queue2'},
    },
)

# 配置周期性任务，　或者定时任务
beat_schedule = {
    'every-5-seconds':
        {
            'task': 'proj.tasks.my_task8',
            'schedule': 5.0,
            # 'args': (16, 16),
        }
}