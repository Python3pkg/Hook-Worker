from distutils.core import setup

setup(
    name='hook_worker',
    version='0.0.1',
    py_modules=['hook_worker_app.py', 'hook_worker_redis.py', 'hook_worker_cmd'],
    url='https://github.com/Capitains/Hook-Worker',
    license='GNU GPL',
    author='Thibault Clerice',
    author_email='leponteineptique@gmail.com',
    description='Lightweight API to handle call and distribute them over a redis server'
)
