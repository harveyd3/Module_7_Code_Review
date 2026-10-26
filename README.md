# Code Review and Documentation Project

## Project Overview
This project highlights reviewing, refactoring, and documenting a Python program.
The goal in this project was to be able to improve readability and maintainability 
while making sure that those changes do not affect the programs original function.

## What the Program Does
The program takes a list of numbers and multiplies even numbers by 2 and odd numbers by 3.
It also takes a list of fruit names, turning all names longer than five characters into uppercase
letters and names with five or fewer get turned to lowercase letters. 

## Files
undocumented_script.py - Refactored Python Program.
CODE_REVIEW.md - Describes issues within the code.
DECISIONS.md - Explains why the code was deigned a certain way during refactoring.

## How to Run the Program
1. Open the undocumented_script.py file in a Python compiler

## Expected Output
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY

## Improvements Made
Renamed functions and variables to make their purposes clearer.
Used a list comprehension for the number calculations.
Added docstrings to explain the purpose of each function.
Verified that the program's output remained unchanged after refactoring.