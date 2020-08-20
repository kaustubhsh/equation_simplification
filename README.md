# equation_simplification
Simple Program to simplify and solve a liner one variable equation in python

## Description
You will be given a JSON file as an input. This file will contain a equation in a structured format like this:




### Notes:
- The operations possible add: add, subtract, multiply, divide, and equal
- Each operation will have a LHS and a RHS. The LHS / RHS of a operation can be:
  - another operation,
  - Or a fixed number,
  - Or a variable reference
- The input files will be limited to have the following characteristics:
  - Top level operation will always be ‘equal’
  - RHS will always be a fixed number
  - LHS can be complex. But there will only be a single variable reference (x) that occurs somewhere in the LHS. All other leaf nodes will be fixed numbers.
  
 ### Setup
 
  Run the following commands :
  
  `python3 parse.py`

