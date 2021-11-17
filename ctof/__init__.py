def cel(x, k=""):
    """
    This function converts the passed value to its Celsius equivalent.
    If optional param "k" is not passed, it is assumed the value is in
    Fahrenheit, otherwise it is assumed the value is in Kelvin.

    :param x: the value to be converted
    :param k: optional, assumes value is in Kelvin if this param is passed
    :type: can be an int, a float or a list/tuple/set with ints or floats
    :return: the Celsius-equivalent value of the passed param
    :rtype: float (list/tuple/set of floats)
    """
    try:
        if k == "":
            if type(x) == list:
                """
                Returns a list with converted numbers (floats).
                The list must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = [float(i) for i in x] # Cast all ints to float
                except ValueError:
                    raise TypeError("List must only contain ints and/or floats")
                for index, item in enumerate(x): # Enumerate list's items
                    x[index] = (x[index] - 32) * 5 / 9 # Convert the enumerated items
                return x
            if type(x) == tuple:
                """
                Returns a tuple with converted numbers (floats)
                The tuple must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = list(x) # Temporarily cast tuple to a list
                    x = [float(i) for i in x] # Cast all ints to float
                except ValueError:
                    raise TypeError("List must only contain ints and/or floats")
                for index, item in enumerate(x): # Enumerate list's items
                    x[index] = (x[index] - 32) * 5 / 9 # Convert the enumerated items
                x = tuple(x) # Convert the list back to a tuple
                return x
            if type(x) == set:
                """
                Returns a set with converted numbers (floats)
                The set must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = list(x)  # Temporarily cast set to a list
                    x = [float(i) for i in x]  # Cast all ints to float
                except ValueError:
                    raise TypeError("List must only contain ints and/or floats")
                for index, item in enumerate(x):  # Enumerate list's items
                    x[index] = (x[index] - 32) * 5 / 9  # Convert the enumerated items
                x = set(x)  # Convert the list back to a set
                return x
            if type(x) == int or float:
                """
                Returns a float
                """
                return (x - 32) * 5 / 9
        else:
            if type(x) == list:
                """
                Returns a list with converted numbers (floats).
                The list must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = [float(i) for i in x] # Cast all ints to float
                except ValueError:
                    raise TypeError("List must only contain ints and/or floats")
                for index, item in enumerate(x): # Enumerate list's items
                    x[index] = x[index] - 273.15 # Convert the enumerated items
                return x
            if type(x) == tuple:
                """
                Returns a tuple with converted numbers (floats)
                The tuple must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = list(x) # Temporarily cast tuple to a list
                    x = [float(i) for i in x] # Cast all ints to float
                except ValueError:
                    raise TypeError("List must only contain ints and/or floats")
                for index, item in enumerate(x): # Enumerate list's items
                    x[index] = x[index] - 273.15 # Convert the enumerated items
                x = tuple(x) # Convert the list back to a tuple
                return x
            if type(x) == set:
                """
                Returns a set with converted numbers (floats)
                The set must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = list(x)  # Temporarily cast set to a list
                    x = [float(i) for i in x]  # Cast all ints to float
                except ValueError:
                    raise TypeError("List must only contain ints and/or floats")
                for index, item in enumerate(x):  # Enumerate list's items
                    x[index] = x[index] - 273.15  # Convert the enumerated items
                x = set(x)  # Convert the list back to a set
                return x
            if type(x) == int or float:
                """
                Returns a float
                """
                return x - 273.15
    except TypeError:
        return "Invalid param type"

def fah(x, k=""):
    """
    This function converts the passed value to its Fahrenheit equivalent.
    If optional param "k" is not passed, it is assumed the value is in
    Celsius, otherwise it is assumed the value is in Kelvin.

    :param x: the Celsius value to be converted
    :param k: optional, assumes value is in Kelvin if this param is passed
    :type: can be an int, a float or a list/tuple/set with ints or floats
    :return: the Fahrenheit-equivalent value of the passed param
    :rtype: float (list/tuple/set of floats)
    """
    try:
        if k == "":
            if type(x) == list:
                """
                Returns a list with converted numbers (floats).
                The list must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = [float(i) for i in x] # Cast all ints to float
                except ValueError:
                    raise TypeError("List must only contain ints and/or floats")
                for index, item in enumerate(x): # Enumerate list's items
                    x[index] = (x[index] * 9 / 5) + 32 # Convert the enumerated items
                return x
            if type(x) == tuple:
                """
                Returns a tuple with converted numbers (floats)
                The tuple must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = list(x) # Temporarily cast tuple to a list
                    x = [float(i) for i in x] # Cast all ints to float
                except ValueError:
                    raise TypeError("Tuple must only contain ints and/or floats")
                for index, item in enumerate(x): # Enumerate list's items
                    x[index] = (x[index] * 9 / 5) + 32 # Convert the enumerated items
                x = tuple(x) # Convert the list back to a tuple
                return x
            if type(x) == set:
                """
                Returns a set with converted numbers (floats)
                The set must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = list(x)  # Temporarily cast set to a list
                    x = [float(i) for i in x]  # Cast all ints to float
                except ValueError:
                    raise TypeError("Set must only contain ints and/or floats")
                for index, item in enumerate(x):  # Enumerate list's items
                    x[index] = (x[index] * 9 / 5) + 32  # Convert the enumerated items
                x = set(x)  # Convert the list back to a set
                return x
            if type(x) == int or float:
                """
                Returns a float
                """
                return (x * 9 / 5) + 32
        else:
            if type(x) == list:
                """
                Returns a list with converted numbers (floats).
                The list must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = [float(i) for i in x] # Cast all ints to float
                except ValueError:
                    raise TypeError("List must only contain ints and/or floats")
                for index, item in enumerate(x): # Enumerate list's items
                    x[index] = (x[index] - 273.15) * 9/5 + 32 # Convert the enumerated items
                return x
            if type(x) == tuple:
                """
                Returns a tuple with converted numbers (floats)
                The tuple must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = list(x) # Temporarily cast tuple to a list
                    x = [float(i) for i in x] # Cast all ints to float
                except ValueError:
                    raise TypeError("Tuple must only contain ints and/or floats")
                for index, item in enumerate(x): # Enumerate list's items
                    x[index] = (x[index] - 273.15) * 9/5 + 32 # Convert the enumerated items
                x = tuple(x) # Convert the list back to a tuple
                return x
            if type(x) == set:
                """
                Returns a set with converted numbers (floats)
                The set must only contain
                ints and/or floats, or an error
                will be raised
                """
                try:
                    x = list(x)  # Temporarily cast set to a list
                    x = [float(i) for i in x]  # Cast all ints to float
                except ValueError:
                    raise TypeError("Set must only contain ints and/or floats")
                for index, item in enumerate(x):  # Enumerate list's items
                    x[index] = (x[index] - 273.15) * 9/5 + 32 # Convert the enumerated items
                x = set(x)  # Convert the list back to a set
                return x
            if type(x) == int or float:
                """
                Returns a float
                """
                x = cel(x, "K")
                x = fah(x)
                return x
    except TypeError:
        return "Invalid param type"

def kel(x, y):
    """
    This function uses param x as the input value(s), and uses param y to
    determine whether the value(s) is in Celsius or Fahrenheit. It then converts
    the value(s) to its Kelvin equivalent(s)

    :param x: the Celsius/Fahrenheit value to be converted
    :param y: specifies if value is Celsius ("C") or Fahrenheit ("F")
    :type: can be an int, a float or a list/tuple/set with ints or floats
    :return: the Kelvin-equivalent value of the passed param
    :rtype: float (list/tuple/set of floats)
    """
    try:
        if type(y) != str:
            raise TypeError("Invalid param y (must be a string)")
        else:
            if y.upper() == "C": # Celsius to Kelvin
                if type(x) == list:
                    """
                    Returns a list with converted numbers (floats).
                    The list must only contain
                    ints and/or floats, or an error
                    will be raised
                    """
                    try:
                        x = [float(i) for i in x]  # Cast all ints to float
                    except ValueError:
                        raise TypeError("List must only contain ints and/or floats")
                    for index, item in enumerate(x):  # Enumerate list's items
                        x[index] = x[index] + 273.15 # Convert the enumerated items
                    return x
                if type(x) == tuple:
                    """
                    Returns a tuple with converted numbers (floats)
                    The tuple must only contain
                    ints and/or floats, or an error
                    will be raised
                    """
                    try:
                        x = list(x)  # Temporarily cast tuple to a list
                        x = [float(i) for i in x]  # Cast all ints to float
                    except ValueError:
                        raise TypeError("Tuple must only contain ints and/or floats")
                    for index, item in enumerate(x):  # Enumerate list's items
                        x[index] = x[index] + 273.15  # Convert the enumerated items
                    x = tuple(x)  # Convert the list back to a tuple
                    return x
                if type(x) == set:
                    """
                    Returns a set with converted numbers (floats)
                    The set must only contain
                    ints and/or floats, or an error
                    will be raised
                    """
                    try:
                        x = list(x)  # Temporarily cast tuple to a list
                        x = [float(i) for i in x]  # Cast all ints to float
                    except ValueError:
                        raise TypeError("Set must only contain ints and/or floats")
                    for index, item in enumerate(x):  # Enumerate list's items
                        x[index] = x[index] + 273.15  # Convert the enumerated items
                    x = set(x)  # Convert the list back to a tuple
                    return x
                if type(x) == int or float:
                    """
                    Returns a float
                    """
                    return x + 273.15
            if y.upper() == "F": # Fahrenheit to Kelvin
                if type(x) == list or tuple or set:
                    x = cel(x)
                    x = kel(x, "C")
                    return x
                if type(x) == int or float:
                    x = cel(x)
                    return x + 273.15
            else:
                raise ValueError("Invalid param y (must be C or F)")
    except TypeError:
        return "Invalid param x type"
