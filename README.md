# 🎭 Playwright with Python - Daily Roadmap

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

Welcome to the **Playwright with Python Learning Roadmap**! This repository serves as a step-by-step guide and personal journey for learning Playwright automation using Python from the ground up, discovering new concepts and techniques every single day.

## 📖 About This Repository

The goal of this roadmap is to start from the absolute basics of Python programming and gradually advance to mastering end-to-end web testing with Playwright. By following this progression, you will build a solid foundation before diving into complex automation tasks.

## 📂 Course Structure & Syllabus

### Phase 1: Python Basics (Days 1-15)
- **Day 1:** Variables
- **Day 2:** Data Types, Operators, Concatenation, User Input, Deleting Variables
- **Day 3:** Conditional Statements, Formatting Output
- **Day 4:** Loops (`for`, `while`), `range()`, `break`, `continue`, `match` Statement
- **Day 5-6:** Strings and String Methods
- **Day 7:** Lists
- **Day 8:** Sets, Tuples
- **Day 9:** Dictionaries
- **Day 10:** Functions & Function Arguments
- **Day 11:** Object-Oriented Programming (OOP) Basics
- **Day 12:** Inheritance, Polymorphism
- **Day 13:** Modules and Packages
- **Day 14:** Abstraction, Encapsulation
- **Day 15:** Exception Handling & File I/O

### Phase 2: Pytest Framework (Days 16-17)
- **Day 16:** Pytest Basics, Fixtures, Scope, `yield` and Returns
- **Day 17:** Advanced Pytest - Grouping, Ordering, and Skipping Tests

### Phase 3: Playwright Fundamentals (Days 18-35)
- **Day 18:** Introduction to Playwright (Sync vs Async)
- **Day 19:** Playwright Locators
- **Day 20:** CSS Selectors
- **Day 21:** XPath Selectors
- **Day 22:** Interacting with Input Boxes, Checkboxes, and Radio Buttons
- **Day 23:** Dropdowns (Single, Multi-selection, Sorted)
- **Day 24:** Hidden Dropdowns
- **Day 25:** Static Web Tables
- **Day 26:** Dynamic Web Tables
- **Day 27:** Date Pickers
- **Day 28:** Dialogs (Alerts) and Frames (iFrames)
- **Day 29:** Mouse Actions
- **Day 30:** Keyboard Actions, File Uploads, and Downloads
- **Day 31:** Browser Contexts, Popups, and Authentication Popups
- **Day 32:** Screenshots, Video Recording, and Tracing
- **Day 33:** Data-Driven Testing
- **Day 34:** HTML Reporting
- **Day 35:** Page Object Model (POM) Design Pattern

## 💻 Prerequisites

To run the examples in this repository, you will need:
- **Python 3.7+** installed on your system.
- An IDE such as **VS Code** or **PyCharm**.

To install the required packages:
```bash
pip install pytest playwright pytest-playwright pytest-html
playwright install
```

## 🛠️ How to Use

Navigate into the respective `Day` folders and run the Python scripts or Pytest files to see the examples in action:

```bash
# Example for running a basic Python script
cd "Day 1"
python variables.py

# Example for running a Pytest file
cd "Day 18"
pytest test_playwright.py
```

## 🤝 Next Steps

Keep checking back! The course is progressively evolving into building an advanced and robust Playwright automation framework. Happy coding! 🎉