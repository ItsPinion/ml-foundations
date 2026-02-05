# ML Foundations — Python & Problem Solving (Month 1)

## Overview

This repository represents my **Month 1 foundations phase** focused on building **strong Python fundamentals, problem‑solving discipline, and clean GitHub practices**.

The objective of this phase was not advanced machine learning, but to establish a **reliable technical base** required for ML, research, and backend‑oriented roles:

* Write clear, correct Python code
* Develop consistency through daily commits
* Practice algorithmic thinking via LeetCode
* Maintain documentation that is readable by reviewers

This repository is intended to be **scanned quickly by recruiters or researchers** and understood without additional explanation.

---

## Skills Demonstrated

### Python Programming

* Core syntax: variables, conditionals, loops
* Data structures: lists, dictionaries, tuples, sets
* Functions: parameters, return values, defaults
* String manipulation and validation

### Code Quality & Structure

* Modular, readable notebooks
* Clear naming conventions
* Incremental refactoring and cleanup
* Comments and basic docstrings where appropriate

### File I/O & Defensive Programming

* Reading and writing files using `open()` and `with`
* Safe handling of runtime errors using `try / except / finally`
* Writing code that fails predictably rather than crashing

### Tooling & Engineering Habits

* Daily Git commits with meaningful messages
* Consistent file and folder structure
* Progressive improvement rather than one‑off scripts
* Documentation as part of development, not an afterthought

### Problem Solving (LeetCode)

* Arrays and strings
* Two‑pointer techniques
* Frequency counting and basic hash maps
* Emphasis on clarity and correctness

---

## Notebooks

The `notebooks/` directory contains **concept-driven Jupyter notebooks** used to build and validate Python fundamentals. Each notebook is scoped to a specific concept and is written to be readable by someone reviewing the repository.

Structure (partial):

```
notebooks/
├── python_basics.ipynb
├── functions_basics.ipynb
├── oop_basics.ipynb
├── file_io_reading.ipynb
├── error_handling.ipynb
├── strings_deep_dive.ipynb
├── sample_text/
│   ├── sample.txt
│   ├── data.txt
│   ├── learning_log.txt
│   └── ...
└── ...
```

Notebook descriptions:

* [`python_basics.ipynb`](./notebooks/python_basics.ipynb) — Core Python syntax: variables, data types, conditionals, and loops. Establishes baseline fluency.
* [`functions_basics.ipynb`](./notebooks/functions_basics.ipynb) — Function definitions, parameters, return values, and basic decomposition of logic.
* [`oop_basics.ipynb`](./notebooks/oop_basics.ipynb) — Object-oriented programming concepts including classes, objects, and instance methods.
* [`file_io_reading.ipynb`](./notebooks/file_io_reading.ipynb) — Reading files, file modes, and basic text processing using real input files.
* [`error_handling.ipynb`](./notebooks/error_handling.ipynb) — Exception handling with `try / except / finally` and defensive programming patterns.
* [`strings_deep_dive.ipynb`](./notebooks/strings_deep_dive.ipynb) — String manipulation, slicing, validation, and common string-based problem patterns.

Supporting text and data files used by notebooks are stored in:

* [`notebooks/sample_text/`](./notebooks/sample_text)

---

## How to Run the Notebooks

### Requirements

* Python **3.10+**
* Jupyter Notebook

### Setup

```bash
# Optional but recommended
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows

pip install notebook
```

### Run

```bash
jupyter notebook
```

Open any notebook from the [`notebooks/`](./notebooks) directory.

---

## Repository Structure

```
ml-foundations/
│
├── notebooks/     # Python concepts and structured practice
├── leetcode/      # LeetCode problem solutions
├── modules/       # Python modules and exercises
├── requirements.txt
├── README.md
```

* [`notebooks/`](./notebooks) — Concept-driven Jupyter notebooks with explanations and examples
* [`leetcode/`](./leetcode) — Algorithm and data-structure practice problems
* [`modules/`](./modules) — Python module and package exercises
* [`requirements.txt`](./requirements.txt) — Python dependencies
* [`README.md`](./README.md) — Project documentation

Each directory is intentionally scoped and self-contained.

---

## LeetCode Practice

Alongside concept learning, I solved **LeetCode problems regularly** to reinforce algorithmic thinking and Python fluency.

Example structure (partial):

```
leetcode/
├── best-time-to-buy-and-sell-stock.py
├── contains-duplicate.py
├── fizz-buzz.py
├── jewels-and-stones.py
├── merge-strings-alternately.py
├── palindrome-number.py
├── roman-to-integer.py
├── two-sum.py
├── valid-anagram.py
├── valid-palindrome.py
└── ...
```

Open any problem from the [`leetcode/`](./leetcode) directory.

Solutions prioritize:

* Correctness
* Readable logic
* Minimal but explicit implementation

---

## Current Status

* Month 1 foundations completed
* ~20 LeetCode Easy problems solved
* Multiple cleaned and refactored notebooks
* Consistent commit history demonstrating discipline

This repository serves as a **baseline proof of fundamentals** and will be extended with data analysis, ML concepts, and projects in subsequent phases.

---

## Reviewer Notes

* This repository focuses on **foundational correctness**, not advanced optimization
* Code is written to be understandable rather than clever
* Later repositories will demonstrate ML depth and system design

The intent here is to show *how I build habits and foundations*, not to overstate experience.
