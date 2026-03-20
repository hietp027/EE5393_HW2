"""
EE 5393 - Circuits, Computation, and Biology
Homework 2 - Due 3/20/26
Grant Hietpas

Problem 2
This script tests my solution for a system of chemical reactions that executes
a biquad filter as described in the problem statement. It uses the simulation code 
in reaction_system.py to demonstrate this system.

AI credit:
- all classes and syntax from reaction_system.py was written by ChatGPT
- minor syntax for state modifications performed in experimental for loop 
"""

from reaction_system import Reaction, ReactionSystem
import matplotlib.pyplot as plt

state_i = {
    'X': 0,
    'Xp': 0,
    'A': 0,
    'D': 0,
    'Y': 0,
    'Dp': 0,
    'Xabs': 0,
    'Dpp': 0,
    'F': 0,
    'C': 0,
    'Dppp': 0,
    'H': 0,
    'E': 0
}

reactions = [
    # X → X'
    Reaction('R1', {'X':1}, {'Xp':1}, 3),

    # X' → D + A
    Reaction('R2', {'Xp':1}, {'D':1,'A':1}, 2),
    #Reaction('R2', {'X':1}, {'D':1,'A':1}, 2),

    # 8A → Y
    Reaction('R3', {'A':8}, {'Y':1}, 1),

    # D + Xabs → D' + Xabs
    Reaction('R4', {'D':1, 'Xabs':1}, {'Dp':1,'Xabs':1}, 2),

    # D' + X → D'' + F + C + X
    Reaction('R5', {'Dp':1, 'X':1}, {'Dpp':1,'F':1,'C':1,'X':1}, 2),

    # 8F → X'
    Reaction('R6', {'F':8}, {'Xp':1}, 1),

    # 8C → Y
    Reaction('R7', {'C':8}, {'Y':1}, 1),

    # D'' + Xabs → D''' + Xabs
    Reaction('R8', {'Dpp':1, 'Xabs':1}, {'Dppp':1,'Xabs':1}, 2),

    # D''' + X → H + E + X
    Reaction('R9', {'Dppp':1,'X':1}, {'H':1,'E':1,'X':1}, 2),

    # 8H → X'
    Reaction('R10', {'H':8}, {'Xp':1}, 1),

    # 8E → Y
    Reaction('R11', {'E':8}, {'Y':1}, 1),

    # 0 → Xabs
    Reaction('R12', {}, {'Xabs':1}, 4),

    # Xabs + X → X
    Reaction('R13', {'Xabs':1,'X':1}, {'X':1}, 0)
]

system = ReactionSystem(reactions)

x_inputs = [100,5,500,20,250]
y_outputs = []
state = state_i

for x in x_inputs:
    
    state['X'] = x
    state = system.run(state)
    
    y_outputs.append(state.get('Y'))

    state['Y'] = 0
    state['Xabs'] = 0

print(f'inputs: {x_inputs}')
print(f'outputs: {y_outputs}')

FIR_outputs = [50, 52, 252, 260, 135]
plt.figure()
plt.plot(x_inputs,label='Inputs X')
plt.plot(FIR_outputs,label='FIR outputs')
plt.plot(y_outputs,label='Biquad outputs')
plt.xlabel('cycles')
plt.ylabel('number of molecules')
plt.title('Chemical Reaction Systems: Sequential Computation')
plt.legend()
plt.show()