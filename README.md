#  Treasure Search in Grid — Strategy, Reasoning & Tradeoffs

## Problem Statement

We are given an **n × n grid** where one cell contains a hidden treasure.
A robot starts at position **(0, 0)** and can move to adjacent cells (up, down, left, right).

The robot:

* Has **no prior knowledge** of the treasure location
* Only observes its **current cell**
* Must explore the grid to find the treasure

---

##  Thought Process & Approach Evolution

### 1️⃣ Initial Idea: Explore Without Knowledge

Since the robot has **no information about the goal**, the problem becomes a **blind search problem**.

This led to the question:
Thought Approach:-
It can go up,down,left and right
And second thing it may or may not go diagonally

> *How do we explore efficiently when we don’t know where to go?*

---

### 2️⃣ Random Walk (Baseline)

First approach:

* Move randomly until the treasure is found

#### Observation:

* Very simple
* But highly inefficient and unpredictable

👉 Helped establish a **baseline for comparison**

---

### 3️⃣ DFS (Depth-First Search)

Next, I considered DFS:

* Explore deeply in one direction, then backtrack

#### Observation:

* Uses less memory
* But may take a **very long path**

👉 Not suitable when we want efficiency

---

### 4️⃣ BFS (Final Choice ✅)

Then I moved to BFS:

* Explore level-by-level from the starting point

#### Key Insight:

> When no direction or goal information is available, exploration should be **uniform in all directions**.

#### Why BFS is ideal:

* Guarantees **minimum number of steps**
* Systematic exploration
* No bias toward any direction

👉 BFS is the **most appropriate strategy for blind search**

---

### 5️⃣ Considering A* (Important Insight)

At this stage, I explored whether **A*** could improve performance.

A* works using:

* Cost so far + estimated distance to goal (heuristic)

#### Key Issue:

* The robot has **no knowledge of the treasure location**
* So it cannot estimate distance to the goal

👉 No heuristic can be defined

#### Note:
In implementation, the treasure location is first identified in the grid so that A* can be demonstrated and compared with BFS.

#### Conclusion:

> Without a heuristic, A* reduces to BFS and provides no advantage.

### 6️⃣ Relation to Dijkstra’s Algorithm

While analyzing A*, I observed:

* A* with **no heuristic (h = 0)** → becomes **Dijkstra’s Algorithm**
* In a grid with equal movement cost → Dijkstra behaves like **BFS**

#### Insight:

> BFS, Dijkstra, and A* are closely related, but differ based on available information.

---

##  Tradeoffs & Complexity

###  Strategy Comparison

| Strategy    | Idea              | Time Complexity | Space  | Optimal | Key Insight           |
| ----------- | ----------------- | --------------- | ------ | ------- | --------------------- |
| Random Walk | Random movement   | Unbounded       | Low    | ❌       | Unreliable            |
| DFS         | Go deep first     | O(n²)           | O(n)   | ❌       | May take long paths   |
| BFS         | Level-wise search | O(n²)           | O(n²)  | ✅       | Best for blind search |
| Dijkstra    | Weighted BFS      | O(n² log n)     | High   | ✅       | Unnecessary here      |
| A*          | Heuristic search  | Depends         | Medium | ✅       | Needs goal knowledge  |

---

##  Why BFS over A*

> A* is often considered more efficient than BFS, but only when a **meaningful heuristic** is available.

In this problem:

* The goal location is **completely unknown**
* No heuristic can guide the search

 Therefore:

* A* behaves exactly like BFS
* Adds complexity without improving performance

---

##  Key Insight

> In a completely unknown environment, **systematic exploration (BFS)** is optimal.
> Intelligent search methods like A* require prior knowledge, which is absent here.

---

## ⚙️ Implementation Summary

* Implemented BFS using a queue
* Tracked visited cells to avoid revisits
* Returned:

  * Treasure location
  * Number of steps taken

---
##  Example Grid

```text
S 0 0 0
0 X 0 0
0 0 0 T
0 X 0 0
```
- S → Start (0,0)
- T → Treasure
- X → Obstacle
- 0 → Free cell

▶️ How to Run

python search.py






