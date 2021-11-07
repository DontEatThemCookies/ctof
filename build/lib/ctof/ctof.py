def cel(x):
    """
    This function assumes the integer or float passed into it is a Fahrenheit value,
    and it is converted to its Celsius equivalent.

    :param x: the Fahrenheit value to be converted
    :type: can be an int, a float or a list/tuple/set with ints or floats
    :return: the Celsius-equivalent value of the passed param
    :rtype: float (list/tuple/set of floats)
    """
    try:
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
    except TypeError:
        return "Invalid param type"

def fah(x):
    """
    This function assumes the integer or float passed into it is a Celsius value,
    and it is converted to its Fahrenheit equivalent.

    :param x: the Celsius value to be converted
    :type: can be an int, a float or a list/tuple/set with ints or floats
    :return: the Fahrenheit-equivalent value of the passed param
    :rtype: float (list/tuple/set of floats)
    """
    try:
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
                raise TypeError("List must only contain ints and/or floats")
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
                raise TypeError("List must only contain ints and/or floats")
            for index, item in enumerate(x):  # Enumerate list's items
                x[index] = (x[index] * 9 / 5) + 32  # Convert the enumerated items
            x = set(x)  # Convert the list back to a set
            return x
        if type(x) == int or float:
            """
            Returns a float
            """
            return (x * 9 / 5) + 32
    except TypeError:
        return "Invalid param type"
