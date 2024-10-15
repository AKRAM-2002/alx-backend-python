#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async
    comprehensions over
    async_generator,
    then returns the list of 10 random numbers.

    Returns:
        List[float]: A list of 10 randomly generated
        float numbers.
    """
    return [num async for num in async_generator()]
