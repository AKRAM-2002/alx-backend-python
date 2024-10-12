#!/usr/bin/env python3
"""
this module contains complex types -list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated function sum_list which takes a list input_list of floats as arg    ument and returns their sum as a float.
    """
    return sum(input_list)
