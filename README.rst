Autobench2
========================

HTTP benchmarking suite for `wrk2 <https://github.com/giltene/wrk2>`_.

Inspired by `Autobench <http://www.xenoclast.org/autobench>`_.

Installation
------------

Autobench2 require `wrk2 <https://github.com/giltene/wrk2>`_ to be installed.

.. code-block::

  $ pip install autobench2

or upgrade to newest version

.. code-block::

  $ pip install --upgrade autobench2

Usage
-----

.. code-block::

  $ autobench --verbose --connection 8 --thread 4 --duration 1m \
              --script wrk.lua --warmup_duration 1m --low_rate 10 \
              --high_rate 20 --rate_step 10 http://example.com/

display help message

.. code-block::

  $ autobench --help

display autobench2 version

.. code-block::

  $ autobench --version
