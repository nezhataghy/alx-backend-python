#!/usr/bin/env python3
"""tasks"""
import asyncio

from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n"""

    dly: List[asyncio.Future[float]] = []
    for _ in range(n):
        dly.append(task_wait_random(max_delay))
    res: List[float] = []
    for delay in asyncio.as_completed(dly):
        res.append(await delay)
    return res
