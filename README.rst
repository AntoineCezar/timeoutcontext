==============
Timeoutcontext
==============

.. image:: https://img.shields.io/travis/AntoineCezar/timeoutcontext.svg
        :target: https://travis-ci.org/AntoineCezar/timeoutcontext

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
        :target: http://timeoutcontext.readthedocs.org/

.. image:: https://img.shields.io/coveralls/AntoineCezar/timeoutcontext.svg
        :target: https://coveralls.io/github/AntoineCezar/timeoutcontext

.. image:: https://img.shields.io/pypi/v/timeoutcontext.svg
        :target: https://pypi.python.org/pypi/timeoutcontext


A `signal <https://docs.python.org/library/signal.html#>`_ based
timeout context manager and decorator.

Usage
-----

As a context manager:

.. code:: python

    from timeoutcontext import timeout, TimeoutException
    from time import sleep

    try:
        with timeout(1):
            sleep(2)
    except TimeoutException:
        print('timeout')

As a decorator:

.. code:: python

    from timeoutcontext import timeout, TimeoutException
    from time import sleep

    @timeout(1)
    def wait():
        sleep(2)

    try:
        wait()
    except TimeoutException:
        print('timeout')

License
-------

* Free software: BSD license
