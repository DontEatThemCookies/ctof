# ctof
### A simple library for temperature unit conversion
### [PyPI Library](https://pypi.org/project/ctof/)

![PkgVersion](https://img.shields.io/pypi/v/ctof)
![PythonVersion](https://img.shields.io/pypi/pyversions/ctof)
![PythonImplementation](https://img.shields.io/pypi/implementation/ctof)
![License](https://img.shields.io/pypi/l/ctof)
![Wheel](https://img.shields.io/pypi/wheel/ctof)

***

ctof is a library for inter-conversion of Celsius, Fahrenheit
and Kelvin values. ctof works with ints and floats, as well as lists,
tuples and sets, allowing for multiple values to be
converted at once.

***

### Installation

```
pip install ctof
```

Import with: `import ctof`

### Functions

There are only three functions in the ctof library:

`cel(value, [iskelvin])`
Returns Fahrenheit value converted to Celsius.

`fah(value, [iskelvin])`
Returns Celsius value converted to Fahrenheit.

**New**: `[iskelvin]` is an optional argument.
If this argument is passed, the function assumes the
given value is in Kelvin instead of Celsius or Fahrenheit.

`kel(value, temp)`
Returns Celsius or Fahrenheit value converted to Kelvin

### Tests

```
python -m unittest -v tests/ctof-tests.py
```

### Examples

Convert an integer
```py
import ctof

print(ctof.cel(32)) # Value is in Fahrenheit
# Output: 0.0
print(ctof.fah(0)) # Value is in Celsius
# Output: 32
```
Convert a float
```py
print(ctof.cel(111.11))
# Output: 43.95
print(ctof.fah(38.6))
# Output: 101.48
```

Convert from a variable
```py
var1 = 86
var2 = 38

print(ctof.cel(var1))
# Output: 30.0
print(ctof.fah(var2))
# Output: 100.4
```

Convert from list, tuple and set
```py
mylist = [37, 38, 39]
mytuple = (86, 87, 88)
myset = {32, 64}

print(ctof.cel(mytuple))
# Output: (30.0, 30.555555555555557, 31.11111111111111)
print(ctof.fah(mylist))
# Output: [98.6, 100.4, 102.2]
print(ctof.fah(myset))
# Output: {89.6, 147.2}
```

Formatted (rounded) output
```py
print(round(ctof.cel(86.9125), 3)) # Round method
print("{:.3f}".format(ctof.cel(86.9125))) # Format method
print(ctof.cel(86.9125)) # Raw output

# Both methods return 30.507
# (30.506944444444443 without formatting)
```

Convert to Kelvin from Celsius or Fahrenheit
```py 
print(ctof.kel(0, "C")) # Celsius
# Output: 273.15
print(ctof.kel(32, "F")) # Fahrenheit
# Output: 273.15
```

Convert to Celsius or Fahrenheit from Kelvin
```py
print(ctof.cel(0, "K")) # Kelvin to Celsius
# Output: -273.15
print(ctof.cel([0, 100], "K")) # List of K values
# Output: [-273.15, -173.14999999999998]

print(ctof.fah(32, "K")) # Kelvin to Fahrenheit
# Output: -402.07
print(ctof.fah([32, 212], "K")) # List of K values
# Output: [-402.07, -78.06999999999996]
```