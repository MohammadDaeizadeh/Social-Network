# Final Project Report

## Graph Algorithms in Real Networks

**Project Option:** B — Social Network (Facebook SNAP)

**Author:** Mohammad Daeizadeh

---

## 1. Introduction

Real-world systems such as social networks, transportation systems, and communication platforms can naturally be modeled as graphs. In such graphs, nodes represent entities and edges represent relationships or interactions between them. Graph algorithms provide powerful tools to analyze these systems, understand their structure, and solve optimization problems.

In this project, a real social network dataset from Facebook is modeled as a graph and analyzed using classical graph algorithms. All algorithms are implemented from scratch in Python, without relying on built-in graph algorithm libraries, in accordance with the course requirements.

---

## 2. Dataset Description

The dataset used in this project is the **Facebook Social Network dataset** provided by the Stanford Network Analysis Project (SNAP).

### Dataset Characteristics

* Nodes represent Facebook users
* Edges represent friendship relationships
* The graph is undirected and unweighted
* Number of nodes: approximately 4,039
* Number of edges: approximately 88,234

Each line in the dataset contains a pair of user IDs indicating a friendship connection.

This dataset is well-suited for studying connectivity, information diffusion, and social influence in large-scale networks.

---

## 3. Graph Modeling

The social network is modeled as an **undirected graph** using an adjacency list representation. This choice is efficient for large and sparse graphs and allows fast access to each user’s neighbors.

Formally:

* Each user is represented as a node
* Each friendship is represented as an undirected edge

The adjacency list structure enables efficient implementation of traversal algorithms such as BFS and DFS, which are central to this project.

---

## 4. Task 1 — Network Connectivity Analysis

### 4.1 Objective

The goal of Task 1 is to analyze how information spreads through the social network and to identify key structural properties such as connectivity and influential users.

### 4.2 Algorithms Used

The following algorithms were implemented from scratch:

* **Breadth-First Search (BFS):**
  Used to compute shortest paths in terms of number of hops and to determine how many users are reachable from a given source user.

* **Depth-First Search (DFS):**
  Used to find connected components in the network. An iterative (stack-based) DFS was implemented to avoid recursion depth limitations in Python.

* **Degree Centrality:**
  Measures the number of direct connections each user has and helps identify influential users.

### 4.3 Results and Interpretation

The analysis shows that the majority of users belong to a single large connected component, indicating a highly connected social network. This implies that information originating from a single user can potentially reach a large portion of the network.

Users with high degree centrality act as hubs and play an important role in information dissemination. Removing or targeting such users would significantly affect the flow of information within the network.

### 4.4 Why These Algorithms Are Appropriate

* BFS accurately models real-world information spread where messages propagate through friendships
* DFS efficiently identifies isolated communities
* Degree centrality provides an intuitive measure of social influence

---

## 5. Task 2 — Pair Matching Problem

### 5.1 Objective

The objective of Task 2 is to model and solve a matching problem within the social network. Examples include pairing users into teams or assigning volunteers to tasks based on social constraints.

### 5.2 Graph Modeling as a Flow Network

The matching problem is transformed into a **bipartite graph**, which is then modeled as a flow network:

* A super source node is connected to all nodes in the left group
* A super sink node is connected to all nodes in the right group
* Edges between left and right groups represent allowed pairings
* All capacities are set to 1

### 5.3 Algorithm Used

* **Edmonds–Karp Algorithm:**
  A BFS-based implementation of the Ford–Fulkerson method is used to compute the maximum flow, which corresponds to the maximum matching.

### 5.4 Results and Interpretation

The maximum flow value represents the largest number of valid pairings that can be formed under the given constraints. Bottlenecks in the flow network highlight structural limitations imposed by the social graph, such as insufficient connections between groups.

This approach ensures an optimal and fair matching solution.

---

## 6. Bonus Task — Link Prediction

### 6.1 Objective

The bonus task aims to predict missing or future friendships by combining graph algorithms with simple machine-learning-style features.

### 6.2 Method: Common Neighbors

For two users who are not currently friends, the number of mutual friends is computed. A higher number of common neighbors indicates a higher likelihood that a friendship may form in the future.

This method is simple, interpretable, and widely used as a baseline in link prediction tasks.

### 6.3 Interpretation

The predicted links represent plausible future connections in the social network. Such predictions can be useful for recommendation systems and social network analysis.

---

## 7. Implementation Details and Constraints

* All graph algorithms are implemented manually
* No built-in shortest path, max-flow, or matching functions are used
* The implementation is modular, readable, and well-documented
* Iterative DFS is used to handle large real-world graphs safely

---

## 8. Conclusion

This project demonstrates how classical graph algorithms can be applied to real social networks to analyze connectivity, influence, optimization, and prediction. By using a real dataset and implementing all algorithms from scratch, the project provides both practical insights and a strong understanding of graph algorithm fundamentals.

The results highlight the power of graph-based modeling in understanding complex social systems and solving real-world problems.

---

## 9. References

* Stanford Network Analysis Project (SNAP)
* Course lecture notes on graph algorithms
