# Programming Language Design & Implementation: PA Project

Designing and building an interpreter for a programming language. Our language is named Luci.

Project part-specific readme files are available for the [Lexer](docs/readme_lex.md) and the [Parser](docs/readme_parse.md).

## Syntax Overview

Luci follows a simple syntax, allowing developers to write expressive and efficient code. Here's an overview of its basic syntax components:

- **Variable Assignments**: Assigning values to variables.
- **Expressions**: Arithmetic operations, comparisons, logic expressions, etc.
- **Conditional Statements**: If-elif-el declarations for controlling program flow.
- **Loop Statements**: Scene and from-to declarations for executing code repeatedly.
- **Comments**: Single-line comments for adding explanatory notes to code.

## Example Code
For example, ex4.note contains:
```
x <- 3.3 # Variable assignments
y <- 4.6
z <- 2

if (x =? 3.3 & y =? 2) action z <- 0 cut el action y <- 2 cut
```

When interpreted by Luci:
```
Enter the file name: ../example/ex3.note
x <- 3.3
Result: 3.3
y <- 4.6
Result: 4.6
z <- 2
Result: 2.0
if (x =? 3.3 & y =? 2) action z <- 0 cut el action y <- 2 cut      
Result: 2.0
```

# CREDITS

This project uses the PLY python lexical analyzer generator. The link to the page is below.

https://www.dabeaz.com/ply/

Team is comprised of Dani Strausburger and Isabel Pacheco Mattivi
