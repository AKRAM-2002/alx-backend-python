#!/usr/bin/env python3
"""
Task-based implementation of wait_n using task_wait_random
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay,
    and return the list of all the delays (float values) in
    ascending order using insertion sort.

    Args:
        n (int): The number of coroutines to spawn
        max_delay (int): The maximum delay value for each task

    Returns:
        List[float]: List of delays in ascending order
    """
    delays = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delays)
