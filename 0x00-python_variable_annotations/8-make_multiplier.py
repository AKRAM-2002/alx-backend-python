#!/usr/bin/env python3
"""
This module contains Complex types - functions
"""
from typing import Callable
def make_multiplier(multiplier:float)->Callable[[float],float]:
    """
    Returns a functions that multiplier a float by multiplier
    """
    def multiply(n: float) -> float:
        """Multiplies a float by the given multiplier."""
        return n * multiplier
              
    return multiply
