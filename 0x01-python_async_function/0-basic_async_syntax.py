#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int =10) -> float:
    """
    an asynchronous coroutine that returns delay
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
