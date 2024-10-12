#!/usr/bin/env python3
"""
This module contains TypeVar and annotations for safely_get_value function.
"""
from typing import TypeVar, Any, Union, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely get a value from a dictionary-like object.

    :param dct: Dictionary or Mapping to get the value from.
    :param key: Key to look for in the dictionary.
    :param default: Default value to return if key is not found.
    :return: The value corresponding to the key or default if key
    is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
