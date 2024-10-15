#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    Asynchronous generator that yields a
    random number between 0 and 10, waiting 1
    second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()*10
