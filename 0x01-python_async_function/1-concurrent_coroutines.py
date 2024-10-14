#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay,
    and return the list of all the delays (float values) in
    ascending order using insertion sort.
    """

    delays = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(delays)
