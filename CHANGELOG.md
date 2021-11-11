### 0.1.3 - November 11, 2021
* Fixed a circular import error with the tests
    * Tests can now be run directly, instead of running from the command line.
    * The test filename has been changed: `python -m unittest -v tests/ctof-tests.py`

### 0.1.2 - November 8, 2021
* NEW: Kelvin conversion
    * Syntax: ctof.kel(value, temptype)
    * Valid temptypes: "C", "F"
    * Example: `ctof.kel(0, "C")`
* ~~ctof now stands for Common Temperature Operation Framework~~
    * Still being considered

### 0.1.1 - November 7, 2021
* Explicitly disallow non-operable data types to be passed as params (e.g. str)
* Other miscellaneous changes
