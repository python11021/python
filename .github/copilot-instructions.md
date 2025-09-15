# Copilot Instructions for This Codebase

## Overview
This repository is a collection of Python scripts and modules organized by topic for educational or practice purposes. There is no single application entry point; instead, each file or folder demonstrates a specific Python concept or feature.

## Directory Structure & Key Patterns
- **Top-level scripts**: Standalone Python files (e.g., `debug_01.py`, `games.py`, `sample.py`) for individual exercises or demonstrations.
- **class/**: Object-oriented programming examples. Each file (`class_01.py` ~ `class_06.py`) introduces or builds on class concepts.
- **For/**, **IF/**, **List/**, **Function/**, **Try/**, **tuple_set_dic/**: Each folder contains scripts focused on a specific Python topic (loops, conditionals, lists, functions, error handling, tuples/sets/dicts).
- **No central main.py**: Each file is meant to be run independently.

## Conventions
- File and folder names are lowercase, often with topic and sequence numbers (e.g., `func_01.py`).
- No external dependencies: All code uses only the Python standard library.
- No package/module imports across folders; scripts are self-contained unless importing from a sibling file in the same folder.
- Minimal use of classes except in the `class/` folder.
- No test framework or build system is present.

## Developer Workflows
- **Run scripts**: Open any `.py` file and run it directly (e.g., `python class/class_06.py`).
- **Debugging**: Use VS Code's built-in debugger. No custom launch configurations are required.
- **No automated tests**: Testing is manual by running scripts and observing output.

## Examples
- To run a class example: `python class/class_03.py`
- To try a list operation: `python List/list_2.py`

## Guidance for AI Agents
- When adding new examples, follow the existing naming and folder conventions.
- Keep new scripts self-contained unless extending a specific topic folder.
- Do not introduce external dependencies or complex project structures.
- Reference similar files for style and structure.

## Key Files/Folders
- `class/`, `For/`, `Function/`, `List/`, `Try/`, `tuple_set_dic/`: Topic-based folders with focused examples.
- Top-level `.py` files: Miscellaneous or introductory scripts.

---
If you are unsure about a pattern or need to introduce a new topic, create a new folder with a clear, descriptive name and follow the existing file naming style.
