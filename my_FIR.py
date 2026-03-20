"""
Test code, written by me, to simulate the FIR reaction system that I wrote as an
alternative to the provided FIR reaction system.
"""

from reaction_system import Reaction, ReactionSystem
import matplotlib.pyplot as plt

state_i = {
    'X': 0,
    'Xp': 0,
    'A': 0,
    'C': 0,
    'Y': 0,
    'Xabs': 0,
    'Cp': 0,
}

reactions = [
    # X → X'
    Reaction('R1', {'X':1}, {'Xp':1}, 2),

    # 2X' → A + C
    Reaction('R2', {'Xp':2}, {'A':1,'C':1}, 1),

    # A → Y
    Reaction('R3', {'A':1}, {'Y':1}, 1),

    # C + Xabs → C' + Xabs
    Reaction('R4', {'C':1, 'Xabs':1}, {'Cp':1,'Xabs':1}, 1),

    # C' + X → Y + X
    Reaction('R5', {'Cp':1, 'X':1}, {'Y':1,'X':1}, 1),

    # 0 → Xabs
    Reaction('R5', {}, {'Xabs':1}, 3),

    # Xabs + X → X
    Reaction('R7', {'Xabs':1,'X':1}, {'X':1}, 0),
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

plt.figure()
plt.plot(x_inputs,label='Inputs X')
plt.plot(y_outputs,label='Ouputs Y')
plt.xlabel('cycles')
plt.ylabel('number of molecules')
plt.title('Chemical Reaction System: Two-Tap FIR Filter')
plt.show()