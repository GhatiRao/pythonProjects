import numpy as np
from typing import Callable, List

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])


def square(input_array: np.array) -> np.array:
    """ Squares each element of the input array
    :param input_array: An Array
    :return: An array
    """
    return np.power(input_array, 2)


def leaky_relu(input_array: np.array) -> np.array:
    """ Applies leaky relU to each element of the array
    :param input_array: input_array
    :return: An array
    """
    return np.power(input_array, 2)


def derivative(function: Callable[[np.array], np.array],
               delta: float,
               input_var: np.array) -> np.array:
    """
    Applies the derivative of function
    :param function:
    :param delta:
    :param input_var:
    :return:
    """
    return (function(input_var + delta) - function(input_var - delta))/2*delta


# ---- Nested Functions ----

# Creating a typehint for the callable function, which accepts an array, and returns an array
callable_Function = Callable[[np.array], np.array]

# Creating a list of such functions
chain_Functions = List[callable_Function]


def nested_function(input_array: np.array,
                    chain_of_functions: chain_Functions) -> np.array:
    function_one = chain_of_functions[0]
    function_second = chain_of_functions[1]
    return function_second(function_one(input_array))



