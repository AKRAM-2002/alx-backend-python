#!/usr/bin/env python3
"""
Task-based implementation of wait_n using task_wait_random
"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int):
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
    # Create a list of asyncio tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Await all the tasks and get the results
    delays = await asyncio.gather(*tasks)
    
    # Insertion sort the delays
    sorted_delays = []
    for delay in delays:
        if not sorted_delays:
            sorted_delays.append(delay)
        else:
            for i in range(len(sorted_delays)):
                if delay < sorted_delays[i]:
                    sorted_delays.insert(i, delay)
                    break
            else:
                sorted_delays.append(delay)

    return sorted_delays
