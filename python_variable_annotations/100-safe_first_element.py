#!/usr/bin/env python3
"""
Annotating variables and function with complex types
"""
from typing import Any, Optional, Sequence


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
