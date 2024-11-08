# Recursive implementation of linear search

from typing import Sequence
from searching import data

def recursive_linear_search(arr: Sequence, target: int, idx: int = 0) -> int:
    if idx == len(arr):
        return -1
    if arr[idx] == target:
        return idx
    return recursive_linear_search(arr, target, idx + 1)

result = recursive_linear_search(data, 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
