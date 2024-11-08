# Iterative implementation of linear search

from typing import Sequence
from searching import data

def linear_search(arr: Sequence, target: int) -> int:
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx
    return -1


result = linear_search(data, 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
