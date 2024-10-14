#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, max_delay) -> float:
    """
    Measure the runtime of wait_n and return the average time per call.
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start

    return total_time / n
