# Python AST Generator

A tool for parsing Python code and generating an Abstract Syntax Tree (AST).

## Overview

This project provides a custom implementation of a Python lexer and parser that can analyze Python source code and generate an abstract syntax tree representation. It's designed for educational purposes to understand how compilers and interpreters work under the hood.

## Features

- Lexical analysis (tokenization) of Python code.
- Parsing of tokens into an AST using Top Down parsing (Abstract Syntax tree)
- Support for basic Python syntax including:
  - Variable declarations and assignments
  - Function definitions
  - Control flow statements (if, else, while, for)
  - Imports
  - Classes
  - And more!

## Project Structure

```
python_ast/
├── __init__.py
├── python_ast_main.py  # Main entry point
├── test.py             # Test cases
├── lexer/              # Lexical analysis components
│   ├── __init__.py
│   ├── lexer.py        # Tokenizer implementation
│   └── token.py        # Token definitions
└── parser/             # Parsing components
    ├── __init__.py
    ├── ast_nodes.py    # AST node definitions
    └── parser.py       # Parser implementation
```

## Usage

To analyze a Python file and print its AST:

```bash
python python_ast_main.py path/to/your/python/file.py
```

## Requirements

- Python 3.6 or higher

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues to improve the project.

## License

[MIT License](LICENSE)
