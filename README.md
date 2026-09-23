#  Python Command-Line Calculator

A simple calculator that runs in the terminal. It asks for two numbers and an operation (`+`, `-`, `*`, `/`), prints the result, and lets the user keep calculating until they choose to stop.

---

##  Overview

This project practices core Python fundamentals: user input, type conversion, conditional logic, and repeating a task with a `while` loop.

**How it works:**

1. The user enters two numbers
2. The user chooses an operation: addition, subtraction, multiplication, or division
3. The program prints the result
4. The user is asked whether to calculate again, and the loop repeats while the answer is `yes`

---

## How to Run

Make sure [Python 3](https://www.python.org/downloads/) is installed, then run:

```bash
python calculator.py
```

**Example run**

```
Enter the first number: 10
Enter the second number: 4
Enter an operation (+, -, *, /): /
Result: 2.5
Do you want to calculate again? (yes/no): yes
Enter the first number: 6
Enter the second number: 3
Enter an operation (+, -, *, /): *
Result: 18.0
Do you want to calculate again? (yes/no): no
```

Results are floats, so whole-number answers display with a decimal (for example, `18.0`).

---

##  Concepts Demonstrated

| Concept | Where it appears |
|---|---|
| **User input** | `input()` collects numbers, the operation, and the repeat choice |
| **Type conversion** | `float(...)` turns typed text into numbers, so decimals work too |
| **`while` loop** | Repeats the calculator while `again == "yes"` |
| **`if` / `elif` / `else`** | Chooses the correct operation and handles invalid ones |
| **Arithmetic operators** | `+`, `-`, `*`, `/` |
| **f-strings** | `f"Result: {result}"` formats the output |

---

