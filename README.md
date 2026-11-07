# Simple Command-Line Calculator

A beginner-friendly calculator in Python that runs in the terminal.

## Features

- Seven operations: addition, subtraction, multiplication, division, modulo, power and floor division
- Keeps running until you choose to quit
- Input validation: invalid operators and invalid numbers are caught and you are asked again
- Friendly error messages for division by zero, zero to a negative power, and other edge cases
- Clean output: `8` is shown instead of `8.0`, while decimals like `2.5` are kept
- Calculation history: view it with `h`, clear it with `c`

## Supported operators

| Operator | Operation       | Example      |
|----------|-----------------|--------------|
| `+`      | Addition        | 5 + 3 = 8    |
| `-`      | Subtraction     | 5 - 3 = 2    |
| `*`      | Multiplication  | 5 * 3 = 15   |
| `/`      | Division        | 7 / 2 = 3.5  |
| `%`      | Modulo          | 7 % 2 = 1    |
| `**`     | Power           | 2 ** 3 = 8   |
| `//`     | Floor division  | 7 // 2 = 3   |

Other commands at the operator prompt: `h` (show history), `c` (clear history), `q` (quit).

## Requirements

- Python 3.6 or newer (no extra packages needed)

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```
python calculator.py
```

On some systems you may need to use `python3 calculator.py` instead.

## Example session

```
SIMPLE CALCULATOR

Choose an operation from: (+ - * / % ** //), (h for history), (c for clearing history) or (q to quit)
Enter an operator: +
Enter the first number: 5
Enter the second number: 3
8

Choose an operation from: (+ - * / % ** //), (h for history), (c for clearing history) or (q to quit)
Enter an operator: /
Enter the first number: 7
Enter the second number: 2
3.5

Choose an operation from: (+ - * / % ** //), (h for history), (c for clearing history) or (q to quit)
Enter an operator: h
5 + 3 = 8
7 / 2 = 3.5

Choose an operation from: (+ - * / % ** //), (h for history), (c for clearing history) or (q to quit)
Enter an operator: q
Program Ended
```