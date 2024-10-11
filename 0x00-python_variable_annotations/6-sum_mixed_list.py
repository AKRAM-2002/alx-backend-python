#!/usr/bin/env python3
"""
This module provides a function to sum a list of floats.
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:

        """Function that takes a list of integers and floats and returns their sum as a float."""
    return float(sum(mxd_lst))