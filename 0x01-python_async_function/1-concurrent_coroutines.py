#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Spawn wait_random n times with the specified max_delay,
    and return the list of all the delays (float values) in
    ascending order using insertion sort.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Insertion sort implementation
    sorted_delays = []
    for delay in delays:
        # Insert the delay into the sorted list
        if not sorted_delays:
            sorted_delays.append(delay)
        else:
            # Find the position to insert the delay
            for i in range(len(sorted_delays)):
                if delay < sorted_delays[i]:
                    sorted_delays.insert(i, delay)
                    break
            else:
                # If the delay is greater than all elements, append it
                sorted_delays.append(delay)

    return sorted_delays
