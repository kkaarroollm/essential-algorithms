### Binary search - finds the position of a target value within a sorted array. Half of the array is eliminated in each iteration.

---

**Runtime complexity:**
- O(log n) - Logarithmic time complexity

**Memory complexity:**
- O(log n) - Recursive
- O(1) - Iterative
- O(1) - built-in bisect module

**Disadvantages:**
- Requires a sorted collection

**Advantages:**
- Faster than linear search
- Works on large collections
- Works on collections that support random access
- O(log n) time complexity means it scales well

**Related examples:**
- [Iterative](iterative.py)
- [Recursive](recursive.py)
- [Bisect module](bisect.py)