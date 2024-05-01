#!/usr/bin/env python3
"""
Annotating variables and function with complex types
"""
from typing import Any, Sequence, Optional


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[T]) -> Optional[T]:
    if lst:
        return lst[0]
    else:
        return None
