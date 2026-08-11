# 🔗 Linked Lists — Python

A collection of **Linked List implementations and problem-solving solutions in Python**, created while learning and practicing **Data Structures and Algorithms (DSA)**.

This repository contains implementations of **Singly Linked Lists, Doubly Linked Lists, insertion, deletion, reversal, cycle detection, loop analysis, palindrome checking, intersection, sorting, and other common Linked List problems**.

The problems in this repository were practiced as part of **Striver's A2Z DSA Sheet**, which is a structured roadmap for learning Data Structures and Algorithms.

---

## 📌 About This Repository

This repository is part of my journey of learning and practicing **DSA using Python**.

The main focus is to understand:

* How Linked Lists work internally
* How nodes are connected using references
* How to traverse Linked Lists
* How insertion and deletion work
* How to manipulate `next` and `prev` references
* How to solve common Linked List problems
* How to apply different problem-solving techniques
* How to analyze time and space complexity

The implementations are written in **Python** with an emphasis on understanding the underlying logic rather than simply memorizing solutions.

---

## 📚 Source / Practice Sheet

The problems in this repository are practiced from:

### 📝 Striver's A2Z DSA Sheet

**Striver's A2Z DSA Sheet** provides a structured path for learning DSA, starting from the basics and progressing toward advanced concepts and problem-solving techniques.

This repository focuses specifically on the **Linked List section** of the sheet.

---

## 🧠 Topics Covered

### 1️⃣ Singly Linked List

The repository contains problems covering:

* Creating a Singly Linked List
* Node creation
* Traversing a Linked List
* Inserting a node at the head
* Deleting the head node
* Counting elements
* Searching for an element
* Finding the middle of a Linked List
* Reversing a Linked List
* Removing the middle node
* Removing the Nth node from the end
* Detecting a loop/cycle
* Finding the length of a loop
* Finding the starting point of a loop
* Finding the intersection of two Linked Lists
* Checking whether a Linked List is a palindrome
* Sorting a Linked List
* Sorting a Linked List containing `0`, `1`, and `2`
* Segregating nodes
* Adding numbers represented using Linked Lists

---

### 2️⃣ Doubly Linked List

Problems related to Doubly Linked Lists include:

* Creating a Doubly Linked List
* Insertion in a Doubly Linked List
* Deletion in a Doubly Linked List
* Reversing a Doubly Linked List

---

## 📂 Repository Structure

```text
LINKED_LISTS/
│
├── add_oneNumber.py
├── add_two_ll.py
├── check_element.py
├── count_elements.py
├── delete_head.py
│
├── double_ll_deletion.py
├── double_ll_insertion.py
├── insert_at_head.py
│
├── intersection.py
├── loop_detection.py
├── loop_length.py
├── loop_start_point.py
│
├── middle_of_ll.py
├── palindrome_check.py
├── remove_middle_node.py
├── remove_nth_node.py
│
├── reverse_double_ll.py
├── reverse_single_ll.py
├── seggregate_nodes.py
│
├── single_linked_list.py
├── sort_012.py
└── sort_ll.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ganeshkds84/LINKED_LISTS.git
```

### 2. Navigate to the Repository

```bash
cd LINKED_LISTS
```

### 3. Run a Python File

For example:

```bash
python single_linked_list.py
```

You can execute the other programs in the same way.

---

## 🛠️ Requirements

The implementations are written using **Python** and primarily use the Python standard library.

No external packages are required for the basic programs.

Check your Python installation:

```bash
python --version
```

---

# 📖 Recommended Learning Path

If you are learning Linked Lists from the beginning, you can go through the repository in the following order.

## 🟢 Step 1 — Linked List Fundamentals

Start with:

```text
single_linked_list.py
```

Understand the basic structure:

```text
+------+------+
| data | next | --------+
+------+------+
                         |
                         ▼
                  +------+------+
                  | data | next | ----+
                  +------+------+
                                       |
                                       ▼
                                +------+------+
                                | data | None |
                                +------+------+
```

A node generally contains:

```python
data
next
```

`data` stores the value, while `next` stores a reference to the next node.

---

## 🟢 Step 2 — Basic Operations

Next, practice:

```text
insert_at_head.py
delete_head.py
count_elements.py
check_element.py
```

These programs help build an understanding of:

* Insertion
* Deletion
* Traversal
* Searching
* Counting nodes

---

## 🟡 Step 3 — Linked List Manipulation

Then move to:

```text
middle_of_ll.py
reverse_single_ll.py
remove_middle_node.py
remove_nth_node.py
```

These problems introduce important techniques for manipulating node references.

---

## 🟡 Step 4 — Important Linked List Techniques

Next, practice:

```text
loop_detection.py
loop_length.py
loop_start_point.py
intersection.py
palindrome_check.py
```

These problems introduce techniques such as:

* Fast and Slow Pointer
* Two Pointer Technique
* Cycle Detection
* Reference comparison
* Linked List reversal
* Efficient traversal

---

## 🔴 Step 5 — Sorting & Rearrangement

Continue with:

```text
sort_ll.py
sort_012.py
seggregate_nodes.py
```

These problems focus on rearranging and sorting nodes efficiently.

---

## 🔴 Step 6 — Doubly Linked Lists

Finally, practice:

```text
double_ll_insertion.py
double_ll_deletion.py
reverse_double_ll.py
```

Here, each node maintains references to both:

```text
previous node
      ↑
      |
+-----+------+------+
| prev | data | next |
+------+------+------+
             |
             ▼
        next node
```

This helps understand how **bidirectional traversal** works.

---

# ⚡ Important Concepts Practiced

While solving these problems, several important DSA techniques are used.

### 🔹 Traversal

Moving from one node to another using the `next` reference.

### 🔹 Two Pointer Technique

Using two references/pointers to solve problems efficiently.

For example:

```text
slow → one step
fast → two steps
```

This technique is useful for:

* Finding the middle
* Detecting cycles
* Finding cycle starting points

### 🔹 Fast & Slow Pointer

A particularly important technique for Linked List problems.

### 🔹 In-place Manipulation

Changing node references without creating unnecessary additional data structures.

### 🔹 Recursion

Some Linked List problems can also be solved using recursive approaches.

### 🔹 Reference Manipulation

Understanding how Python variables reference objects is essential for correctly manipulating Linked Lists.

---

# ⏱️ Complexity

Typical complexities for a Singly Linked List:

| Operation             | Time Complexity |
| --------------------- | --------------: |
| Access by position    |            O(n) |
| Search                |            O(n) |
| Insert at beginning   |            O(1) |
| Delete from beginning |            O(1) |
| Insert at end*        |            O(n) |
| Delete from end*      |            O(n) |
| Traversal             |            O(n) |

*Complexity can change if a `tail` reference is maintained.

---

# 🎯 Learning Goals

Through this repository, I am working toward building a strong foundation in:

* Data Structures
* Algorithms
* Problem Solving
* Python Programming
* Time & Space Complexity
* Pointer/Reference Manipulation
* Interview-oriented DSA

The ultimate goal is not just to solve individual problems, but to understand the **patterns and techniques behind them** so that they can be applied to new problems.

---


---

# 🤝 Contributions

This repository is primarily maintained as a personal learning and practice repository.

Suggestions, improvements, corrections, and additional problem-solving approaches are welcome.

Feel free to open an **Issue** or submit a **Pull Request** if you find something that can be improved.

---

# ⭐ Support

If this repository helps you learn or revise Linked Lists, consider giving it a ⭐ on GitHub.

---

## 📜 Disclaimer

The problems practiced in this repository are based on the **Linked List section of Striver's A2Z DSA Sheet**.

The implementations in this repository are my own practice implementations created for **learning, understanding, and revision purposes**.

---

### 🚀 Keep Learning. Keep Practicing. Keep Building.

**Happy Coding! 🐍💻**
