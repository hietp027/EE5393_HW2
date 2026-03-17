"""
EE 5393 - Circuits, Computation, and Biology
Homework 2 - Due 3/20/26
Grant Hietpas

Problem 1
This script tests my solution for a system of chemical reactions that executes
the Fibonacci sequence for a certain number of steps. It uses the simulation code 
in reaction_system.py to demonstrate this system.

AI credit:
- all classes and syntax from reaction_system.py was written by ChatGPT
"""

from reaction_system import Reaction, ReactionSystem
import math

x1 = 0
x2 = 1
n = 11  # number of steps to be executed

state = {
    'x1': x1,
    'x2': x2,
    'n': n-1, 
    'y': 0,
    'x2_prime': 0,
    'x_abs':0,
}

reactions = [
    Reaction(
        name='R1',
        reactants={'x1': 1},
        products={'y': 1},
        priority=2
    ),
    Reaction(
        name='R2',
        reactants={'x2': 1},
        products={'y': 1,'x2_prime': 1},
        priority=2
    ),
    Reaction(
        name='R3',
        reactants={'n': 1},
        products={'n': 1,'x_abs': 1},
        priority=3
    ),
    Reaction(
        name='R4',
        reactants={'x2_prime': 1,'x_abs': 1},
        products={'x1': 1,'x_abs': 1},
        priority=0
    ),
        Reaction(
        name='R5',
        reactants={'y': 1,'x_abs': 1},
        products={'x2': 1,'x_abs': 1},
        priority=0
    ),
        Reaction(
        name='R6',
        reactants={'x1': 1,'x_abs': 1,'n': 1},
        products={'x1': 1},
        priority=1
    ),
    Reaction(
        name='R7',
        reactants={'x2': 1,'x_abs': 1,'n': 1},
        products={'x2': 1},
        priority=1
    )
]

system = ReactionSystem(reactions)
final_state = system.run(state)

print("Final state:")
for k, v in final_state.items():
    print(f"  {k}: {v}")

ni = n
x1i = x1
x2i = x2
while ni>0:
    yi = x1i + x2i
    x1i = x2i
    x2i = yi
    ni -= 1
y_expected = yi

print(f"\nExpected y = {n}th step of Fibonacci sequence starting with {x1} and {x2} = {y_expected}")