# Algorithms and Data Structures

This repository contains exercises, concepts, and implementations of algorithms and data structures in **Python**.
Problems and exercises are sourced from platforms such as **LeetCode, Codecademy, Educative, and DataCamp**.

The goal of this repository is to strengthen problem-solving skills and build a structured reference for common algorithm patterns and data structures.

## Topics Covered

* Arrays and Strings
* Hash Tables
* Linked Lists
* Stacks and Queues
* Trees and Graphs
* Recursion
* Sorting Algorithms
* Searching Algorithms
* Dynamic Programming

## Structure

```
algorithms-and-data-structures/
│
├── leetcode/
│   ├── arrays/
│   ├── strings/
│   ├── hash_tables/
│   ├── linked_lists/
│   ├── trees/
│   ├── graphs/
│   └── dynamic_programming/
│
├── codecademy/
│   ├── recursion/
│   ├── sorting/
│   └── searching/
│
├── educative/
│   ├── sliding_window/
│   ├── two_pointers/
│   ├── fast_slow_pointers/
│   └── merge_intervals/
│
├── datacamp/
│   ├── python_algorithms/
│   └── data_structures/
│
├── implementations/
│   ├── sorting/
│   ├── searching/
│   └── data_structures/
│
└── notes/
    ├── time_complexity.md
    ├── algorithm_patterns.md
    └── big_o_cheatsheet.md
```

## Example Problem

Example: **Two Sum**

```python
# LeetCode 1
# Topic: Hash Table

def twoSum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]

        lookup[num] = i
```

---

## Learning Sources

Problems and exercises are derived from:

* LeetCode
* Codecademy
* Educative
* DataCamp

---

## Goals

* Practice algorithmic problem solving
* Understand common data structure patterns
* Improve Python implementation skills
* Prepare for technical interviews

---

## License

This project is licensed under the MIT License.