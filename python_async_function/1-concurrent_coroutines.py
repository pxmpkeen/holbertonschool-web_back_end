#!/usr/bin/env python3
"""
Async: beginning
"""
from 0-basic_async_syntax import wait_random
import asyncio
import random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async func v2
    """
    delays: List[float] = list()
    [delays.append(await wait_random(max_delay)) for mirt in range(n)]
    return sorted(delays)
