#!/usr/bin/env python3
"""
Python AST Generator 

This module provides a command-line interface for parsing Python code
and generating an Abstract Syntax Tree (AST).
"""

import sys
import argparse
from lexer.lexer import Lexer
from parser.parser import Parser

def read_file(filename):
    """Read content from a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # Parse command line arguments
    arg_parser = argparse.ArgumentParser(
        description='Generate AST for Python code.'
    )
    arg_parser.add_argument(
        'input_file', 
        help='Path to the Python source file'
    )
    args = arg_parser.parse_args()

    try:
        # Read source code from input file
        source = read_file(args.input_file)
        
        # Create lexer and tokenize the source
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Print tokens if needed for debugging
        # for token in tokens:
        #     print(f"{token.type}: '{token.value}' at line {token.line}, column {token.column}")
        
        # Create parser and parse tokens into AST
        parser = Parser(tokens)
        ast_nodes = parser.parse()
        
        # Print the AST
        print(f"Abstract Syntax Tree for {args.input_file}:")
        print("-" * 50)
        for node in ast_nodes:
            node.print_node()
        
    except FileNotFoundError:
        print(f"Error: Could not open file {args.input_file}")
        return 1
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())