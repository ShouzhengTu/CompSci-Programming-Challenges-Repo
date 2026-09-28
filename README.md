# CompSci Programming Challenges Repo

This repository contains a small collection of weekly Computer Science programming assignments and practice exercises. The projects are focused on interactive Python programs, file-based data storage, and basic problem-solving tasks.

## Repository Purpose

The goal of this repo is to store and organize coursework completed over multiple weeks. Each folder represents a different assignment, and each assignment includes a Python script and supporting data files.

## Repository Structure

```text
CompSci-Programming-Challenges-Repo/
├── LICENSE
├── README.md
├── week2 homework/
│   ├── Shopping_List.py
│   └── stock.txt
├── week3 homework/
│   ├── Student Grade Management System(CompSci).py
│   └── grades.txt
└── week4 homework/
    └── placeholder
```

## Week-by-Week Overview

### Week 2: Shopping List / Inventory Manager

Location: `week2 homework/Shopping_List.py`

This script simulates a simple shopping and inventory system. It lets the user:

- view the current stock catalog
- add new items to inventory
- buy items from the catalog
- calculate subtotal and discount-based totals
- save inventory updates to `stock.txt`

The inventory data is stored in `week2 homework/stock.txt`, where each line follows this format:

```text
item_name,price,quantity
```

Example usage:

```bash
cd "week2 homework"
python "Shopping_List.py"
```

### Week 3: Student Grade Management System

Location: `week3 homework/Student Grade Management System(CompSci).py`

This script acts as a basic student grade tracker. It provides a menu-based interface for:

- viewing all student grades
- adding new grades for a student
- calculating individual statistics
- performing global grade analysis

It reads and writes data from `week3 homework/grades.txt`, where each line contains a comma-separated list of grades for one student.

Example usage:

```bash
cd "week3 homework"
python "Student Grade Management System(CompSci).py"
```

### Week 4

Location: `week4 homework/placeholder`

This folder currently contains a placeholder file, indicating that the assignment for this week has not been populated yet.

## Programming Language

These assignments are written in Python and are designed to run from the terminal using standard Python 3.

## Notes

- File and folder names with spaces should be referenced with quotes in shell commands.
- The projects are simple, beginner-friendly exercises centered on Python logic, file I/O, and user interaction.
- The repo is intended as a personal archive of weekly coursework and class activities.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
