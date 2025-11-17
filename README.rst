==============
Timeoutcontext
==============

.. image:: https://img.shields.io/pypi/v/timeoutcontext.svg
        :target: https://pypi.python.org/pypi/timeoutcontext


A `signal <https://docs.python.org/library/signal.html#>`_ based
timeout context manager and decorator.

Since it is signal based this package can not work under Windows operating
system.

Usage
-----

As a context manager:

.. code:: python

    import sys
    from time import sleep
    rom timeoutcontext import timeout

    try:
        with timeout(1):
            sleep(2)
    except TimeoutError:
        print('timeout')

As a decorator:

.. code:: python

    import sys
    from time import sleep
    from timeoutcontext import timeout

    @timeout(1)
    def wait():
        sleep(2)

    try:
        wait()
    except TimeoutError:
        print('timeout')

License
-------

* Free software: BSD license
