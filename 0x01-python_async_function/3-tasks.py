#!/usr/bin/env python3
"""
Task to wrap wait_random
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that wraps the wait_random coroutine

    Args:
        max_delay (int): The maximum delay

    Returns:
        asyncio.Task: An asyncio Task
    """
    return asyncio.create_task(wait_random(max_delay))
