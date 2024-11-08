# Recursive linear search using regex

import re
from typing import Sequence

from searching import str_data

def regex_linear_search(arr: Sequence[str], pattern: str) -> int:
    regex = re.compile(pattern)

    for idx, elem in enumerate(arr):
        if regex.search(elem):
            return idx
    return -1

result = regex_linear_search(str_data, "pina")

if result != -1:
    print(f"Element found at idx: {result}")
else:
    print("Not found")
