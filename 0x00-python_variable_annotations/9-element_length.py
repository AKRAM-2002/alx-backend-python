#!/usr/bin/env python3
"""
the module contains Iterable object
"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from lst and its length
    """
    return [(i, len(i)) for i in lst]
