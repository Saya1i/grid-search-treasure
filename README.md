# Grid Search: Finding Treasure

## Problem

A robot starts at (0,0) in an n x n grid and must find a treasure.
It can move to neighboring cells and only knows its current position.

---

## Approach

I started with **Breadth-First Search (BFS)**, which guarantees the shortest path when all moves have equal cost.

However, BFS explores the grid uniformly and does not account for different movement costs.

To improve this, I implemented **A*** search, which uses a heuristic (distance to the goal) to guide the search more efficiently.

---

## Trade-offs

* **BFS**

  * Guarantees shortest path
  * Explores many unnecessary cells
  * Higher memory usage

* **A***

  * Faster and more efficient
  * Uses heuristic to guide search
  * Slightly more complex

---

## Extensions

* Added **diagonal movement**
* Implemented **A*** for weighted paths
* Added **path reconstruction** (like GPS route)

---

## How to Run

Run the following:

```bash
python search.py
```

---

## Key Insight

BFS works well for simple cases, but when movement costs differ or efficiency is important, A* provides a better solution by combining cost and goal direction.
