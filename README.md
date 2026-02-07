# 🤝 Social Network Graph Algorithms Project

## Overview

This project is a complete implementation of **graph algorithms on a real-world social network**, developed as a final course project for *Graph Algorithms in Real Networks*.

The Facebook SNAP dataset is modeled as an **undirected, unweighted graph**, where:

* **Nodes** represent users
* **Edges** represent friendship relationships

All core algorithms are implemented **from scratch**, strictly following course rules. No built-in graph algorithms (e.g., NetworkX shortest path, max-flow, or matching) are used.

---

## Dataset

**Facebook Social Network (SNAP)**

* Source: Stanford Network Analysis Project (SNAP)
* File: `facebook_combined.txt`
* Nodes: ~4,039 users
* Edges: ~88,234 friendships
* Graph type: Undirected, unweighted

Each line in the dataset represents a friendship between two users:

```
userA userB
```

---

## Project Structure

```
Social-Network-Graph/
│
├── SN.py                  # Main Python implementation
├── facebook_combined.txt  # Dataset (downloaded separately)
└── README.md              # Project documentation
```

---

## Graph Modeling

The social network is represented using an **adjacency list**:

* Efficient for large sparse graphs
* Natural representation of friendships
* Supports fast neighbor lookups

```python
adj[node] = {neighbor1, neighbor2, ...}
```

---

## Implemented Algorithms

All algorithms below are implemented manually, without external graph libraries.

### 1. Breadth-First Search (BFS)

* Computes shortest paths (minimum number of hops)
* Models **information spread** in the network
* Used to measure reachability from a given user

### 2. Depth-First Search (DFS — Iterative)

* Used to find **connected components**
* Implemented iteratively to avoid Python recursion limits
* Identifies isolated communities in the network

### 3. Degree Centrality

* Measures number of direct friends per user
* Identifies influential or highly connected users

### 4. Max-Flow (Edmonds–Karp Algorithm)

* BFS-based Ford–Fulkerson implementation
* Used to solve matching problems
* Implemented on a residual flow network

---

## Task 1 — Network Connectivity Analysis

This task analyzes how information flows through the social network.

### What is computed:

* Number of users reachable from a given source user
* Total number of connected components
* Size of the largest component
* Top central (high-degree) users

### Interpretation:

* Large connected components indicate strong global connectivity
* Central users act as hubs for information spread
* BFS models realistic social diffusion processes

---

## Task 2 — Pair Matching Problem

This task models problems such as:

* Team formation
* Volunteer-task assignment
* Pairing users under constraints

### Modeling approach:

* The problem is converted into a **bipartite graph**
* A **flow network** is constructed with:

  * Source → left group
  * Right group → sink
  * Edges represent allowed pairings

### Solution:

* Maximum matching is found using **Edmonds–Karp max-flow**
* The resulting flow represents optimal pairings

---

## Bonus Task — Link Prediction

An optional bonus task that combines graph algorithms with basic machine-learning-style features.

### Method: Common Neighbors

For two users `u` and `v`:

* Count the number of mutual friends
* Higher count ⇒ higher probability of future friendship

### Output:

* Ranked list of predicted missing edges
* Interpretable and explainable predictions

---

## How to Run the Project

1. Download the dataset from SNAP:
   [https://snap.stanford.edu/data/egonets-Facebook.html](https://snap.stanford.edu/data/egonets-Facebook.html)

2. Extract `facebook_combined.txt` and place it next to `SN.py`

3. Run the program:

```bash
python SN.py
```

---

## Example Output

```
Network Connectivity Analysis
reachable_users: 4039
number_of_components: 1
largest_component_size: 4039
top_central_users: [...]

Maximum matching size: 43

Predicted missing friendships:
12 98 score: 7
45 301 score: 6
```

---

## Course Compliance

✔ Real-world dataset
✔ Two required tasks completed
✔ Bonus task implemented
✔ No built-in graph algorithms used
✔ Clean, modular, readable code

---

## Conclusion

This project demonstrates how classical graph algorithms can be applied to real social networks to analyze connectivity, influence, optimization, and prediction. The implementation emphasizes correctness, interpretability, and strict adherence to academic rules.

---

## 👨‍💻 Contributors
* **Mohammd Daeizadeh** - Developer


## ✅ Acknowledgments
* **Dr. Maryam Tahmasbi**
