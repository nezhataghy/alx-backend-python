#!/usr/bin/env python3
"""concurrent_coroutines"""
import asyncio

from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n"""

    delays: List[asyncio.Future[float]] = []
    for _ in range(n):
        delays.append(wait_random(max_delay))

    result: List[float] = []
    for delay in asyncio.as_completed(delays):
        result.append(await delay)
    return result
