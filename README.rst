
ctof 0.2.0
==========

A simple library for temperature unit conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`PyPI Library <https://pypi.org/project/ctof/>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. image:: https://img.shields.io/pypi/v/ctof
   :target: https://img.shields.io/pypi/v/ctof
   :alt: PkgVersion


.. image:: https://img.shields.io/pypi/pyversions/ctof
   :target: https://img.shields.io/pypi/pyversions/ctof
   :alt: PythonVersion


.. image:: https://img.shields.io/pypi/implementation/ctof
   :target: https://img.shields.io/pypi/implementation/ctof
   :alt: PythonImplementation


.. image:: https://img.shields.io/pypi/l/ctof
   :target: https://img.shields.io/pypi/l/ctof
   :alt: License


.. image:: https://img.shields.io/pypi/wheel/ctof
   :target: https://img.shields.io/pypi/wheel/ctof
   :alt: Wheel


----

ctof is a library for inter-conversion of Celsius, Fahrenheit
and Kelvin values. ctof works with ints and floats, as well as lists,
tuples and sets, allowing for multiple values to be
converted at once.

----

Installation
^^^^^^^^^^^^

.. code-block::

   pip install ctof

Import with: ``import ctof``

Functions
^^^^^^^^^

There are only a couple of functions in ctof 0.2.0:

``ctof.convert(values, _from, _to)`` \
This function is the entire ctof library's core functionality.
``values`` can be an int, float or a list/tuple/set of ints/floats.
``_from`` and ``_to`` indicate the temperature to convert from and the
temperature to convert to, respectively. They can be "C", "F" or "K".

``ctof.version()`` \
Prints out the current version and release date.

Tests
^^^^^

.. code-block::

   pytest tests/test-ctof.py

Examples
^^^^^^^^

Convert an integer

.. code-block:: py

   import ctof

   print(ctof.convert(32, "F", "C")) # Value is in Fahrenheit
   # Output: 0.0
   print(ctof.convert(0, "C", "F")) # Value is in Celsius
   # Output: 32.0

Convert a float

.. code-block:: py

   print(ctof.convert(111.11, "F", "C"))
   # Output: 43.95

Convert from a variable

.. code-block:: py

   var1 = 86
   var2 = 38

   print(ctof.convert(var1, "F", "C"))
   # Output: 30.0
   print(ctof.convert(var2, "C", "F"))
   # Output: 100.4

Convert from list, tuple and set

.. code-block:: py

   mylist = [37, 38, 39]
   mytuple = (86, 87, 88)
   myset = {273.15, 373.15}

   print(ctof.convert(mytuple, "F", "C"))
   # Output: (30.0, 30.555555555555557, 31.11111111111111)
   print(ctof.convert(mylist, "C", "F"))
   # Output: [98.6, 100.4, 102.2]
   print(ctof.convert(myset, "K", "C"))
   # Output: {0.0, 100.0}

Formatted (rounded) output

.. code-block:: py

   print(round(ctof.convert(86.9125, "F", "C"), 3)) # Round method
   print("{:.3f}".format(ctof.cel(86.9125))) # Format method
   print(ctof.cel(86.9125)) # Raw output

   # Both methods return 30.507
   # (30.506944444444443 without formatting)
