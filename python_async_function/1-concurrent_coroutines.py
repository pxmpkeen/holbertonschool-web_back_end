#!/usr/bin/env python3
"""
Async: beginning
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async func v2
    """
    delays: List[float] = list()
    [delays.append(await wait_random(max_delay)) for mirt in range(n)]
    return sorted(delays)
