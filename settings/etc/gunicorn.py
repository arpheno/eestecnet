import multiprocessing

bind = "0.0.0.0:8003"
timeout = 600
pidfile = "/home/vagrant/gunicorn.pid"
workers = multiprocessing.cpu_count() * 2 + 1
pythonpath = "/vagrant"
# accesslog = "/vagrant/logs/gunicorn-access-log.txt"
# errorlog = "/vagrant/logs/gunicorn-error-log.txt"
reload = True
