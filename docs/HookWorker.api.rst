HookWorker API
=================================

.. _HookWorker.api:

Rest API
########

.. autoclass:: HookWorker.api.WorkerAPI

.. automethod:: HookWorker.api.WorkerAPI.init_app

Controller
----------

.. automethod:: HookWorker.api.WorkerAPI.get_queue
.. automethod:: HookWorker.api.WorkerAPI.check_signature

Routes
------

.. automethod:: HookWorker.api.WorkerAPI.r_delete
.. automethod:: HookWorker.api.WorkerAPI.r_submit

Server Helper
-------------

.. autofunction:: HookWorker.api.set_logging
.. autofunction:: HookWorker.api.run

Worker
######

The worker is a simpler Python RQ based worker

.. autofunction:: HookWorker.worker.worker

