Deploying Hook-Worker
=====================

.. _HookWorker.deployment:

Pre-requisite
-------------

*Warning: you might need to sudo all following commands*

Python and Python tools
***********************

-  Make sure to have python 2.7 **and** python 3

   -  ``apt-get install python3 python2``

-  Make sure to have pip installed for both python 2 and 3

   -  Ubuntu 12.10 and later > ``apt-get install python3-pip``
   -  `Ubuntu
      12.04 <http://askubuntu.com/questions/412178/how-to-install-pip-for-python-3-in-ubuntu-12-04-lts>`__
      ``apt-get install python3-setuptools`` and ``easy_install3 pip``

-  Install virtualenv for python3

   -  ``pip3 install virtualenv``

- Install development dependencies
   - ``sudo apt-get install python-dev libxml2-dev libxslt-dev``

Redis
******

- `Install Redis <http://redis.io/topics/quickstart>`__

Supervisor
**********

-  Install through with pip

   -  ``pip install supervisor``

-  `Configure
   supervisor <http://supervisord.org/installing.html#creating-a-configuration-file>`__

   -  Default configuration can be created with
      ``echo_supervisord_conf > /etc/supervisord.conf``

Configuration of supervisor
***************************

**DO NOT FORGET TO CHANGE THE PASSWORD**

.. code:: cfg

    [unix_http_server]
    file=/tmp/supervisor.sock       ; (the path to the socket file)
    ;chmod=0700                     ; socket file mode (default 0700)
    chown=capitainshook:nogroup     ; socket file uid:gid owner
    username=capitainshook          ; (default is no username (open server))
    password=capitains              ; (default is no password (open server))

    [supervisord]
    logfile=/var/log/supervisord.log ; (main log file;default $CWD/supervisord.log)
    user=capitainshook           ; (default is current user, required if root)

    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

    [supervisorctl]
    serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
    username=capitainshook               ; should be same as http_username if set
    password=capitains                   ; should be same as http_password if set

Hook Worker
-----------

Code base
*********

We advise to set-up a user account only for Hook. This will relieve you
from many security flaws :

-  ``adduser capitainshook``
-  Set-up the password and remember it
-  ``su capitainshook``
-  ``cd /home/capitainshook/``
-  ``virtualenv --python=/usr/bin/python3 venv`` (or ``virtualenv-3.4``)
-  ``source venv/bin/activate``
-  *For logs* : ``mkdir -R logs/api``

- **Using pip**
    -  ``pip install HookWorker``
- **Using git**
    -  ``git clone https://github.com/Capitains/Hook-Worker.git worker``
    -  ``cd worker``
    -  ``python setup.py install``

Services
********

Add the following to your supervisord.conf

The secret should be set to the secret key used by authorized callers of the HookWorker API

.. code:: cfg

    [program:hookworkerapi]
    command=/home/capitainshook/venv/bin/hookworker-api --api --path /home/capitainshook/logs/api/ --port 5002 --level INFO --secret YourSecret --git /home/capitainshook/git --workers 7; Do not forget to change the secret !
    stderr_logfile=/home/capitainshook/logs/api.error.log


    [program:hookworkerrq]
    command=/home/capitainshook/venv/bin/hookworker-api --rq --redis 127.0.0.1:6379
    stdout_logfile=/home/capitainshook/logs/worker.log
    stderr_logfile=/home/capitainshook/logs/worker.error.log

