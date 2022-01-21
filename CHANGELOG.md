# changelog
***

### 0.2.0 - January 21, 2022
* Complete rewrite of the ctof library
  * New usage and syntax detailed in updated README.md
  * By default, all numbers returned are of type float
  * ctof testing is now conducted on PyTest, superseding unittest
  * All versions from 0.2.0 onwards are INCOMPATIBLE with previous ones!

<details><summary>Old Versions</summary>

### 0.1.81 - November 24, 2021
* Fixed error in version() function
* Otherwise, still identical to 0.1.8

### 0.1.80 - November 24, 2021
* PyPI has SOMEHOW messed up the release history
    * 0.1.8 has been re-released as 0.1.80
    * Re-released due to a PyPI bug


### 0.1.8 - November 24, 2021
* Parameters with invalid types are now handled by
  raising a TypeError (e.g. calling the function with
  a string parameter)
* Added header documentation to show up as help.
     * Input `help(ctof)`
* New function `version()` - just prints the lib version

### 0.1.75 - November 17, 2021
* FIXED CRITICAL ISSUE PRESENT IN 0.1.7
    * USE 0.1.75 INSTEAD OF 0.1.7

### 0.1.7 - November 17, 2021
* ctof now supports Kelvin to Celsius/Fahrenheit conversion
    * View the readme for more details

### 0.1.6 - November 13, 2021
* IMPORTANT PATCH: Moved the codebase to `__init__.py`
    * ctof must now be imported as `import ctof`
	* Change your code if it has been made pre-0.1.6

### 0.1.5 - November 11, 2021
* I forgot to change a thing in 0.1.4
    * It has been deleted, but the name couldn't be reused
    * Therefore, 0.1.4 has been re-released as 0.1.5

### 0.1.4 - November 11, 2021
* Very minor patch - added project url

### 0.1.3 - November 11, 2021
* Fixed a circular import error with the tests
    * Tests can now be run directly, instead of running from the command line.
    * The test filename has been changed: `python -m unittest -v tests/ctof-tests.py`

### 0.1.2 - November 8, 2021
* NEW: Kelvin conversion
    * Syntax: ctof.kel(value, temptype)
    * Valid temptypes: "C", "F"
    * Example: `ctof.kel(0, "C")`

### 0.1.1 - November 7, 2021
* Explicitly disallow non-operable data types to be passed as params (e.g. str)
* Other miscellaneous changes
</details>