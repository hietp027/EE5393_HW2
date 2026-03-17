"""
Code providing framework for testing systems of reactions. This code was generated entirely 
by ChatGPT, but required multiple versions worth of my testing and debugging to get working.
Included is a demo of Y = 2^X from HW1 P3 problem statement to prove efficacy of code.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Reaction:
    name: str
    reactants: Dict[str, int]
    products: Dict[str, int]
    priority: int  # lower = faster

    def can_fire(self, state: Dict[str, int]) -> bool:
        return all(state.get(s, 0) >= n for s, n in self.reactants.items())

    def fire_once(self, state: Dict[str, int]):
        for s, n in self.reactants.items():
            state[s] -= n
        for s, n in self.products.items():
            state[s] = state.get(s, 0) + n


class ReactionSystem:
    def __init__(self, reactions: List[Reaction], max_steps: int = 100_000):
        # Sort once by priority
        self.reactions = sorted(reactions, key=lambda r: r.priority)
        self.max_steps = max_steps

    def highest_priority_reaction(self, state: Dict[str, int]) -> Optional[Reaction]:
        for reaction in self.reactions:
            if reaction.can_fire(state):
                return reaction
        return None

    def run(self, state: Dict[str, int]) -> Dict[str, int]:
        steps = 0

        while True:
            reaction = self.highest_priority_reaction(state)

            if reaction is None:
                break  # end state reached

            reaction.fire_once(state)
            steps += 1

            if steps > self.max_steps:
                # raise RuntimeError(
                #     "Reaction system did not terminate. "
                #     "Possible cycle or missing end state."
                # )
                print('WARNING: reaction system did not terminate.')
                break

        return state


def main():
    x0 = 5

    # Seed y with 1
    state = {
        'x': x0,
        'a': 0,
        'y': 1,
        'y_prime': 0
    }

    reactions = [
        Reaction(
            name='autocatalysis',
            reactants={'a': 1, 'y': 1},
            products={'a': 1, 'y_prime': 2},
            priority=0
        ),
        Reaction(
            name='a_decay',
            reactants={'a': 1},
            products={},
            priority=1
        ),
        Reaction(
            name='yprime_to_y',
            reactants={'y_prime': 1},
            products={'y': 1},
            priority=2
        ),
        Reaction(
            name='x_to_a',
            reactants={'x': 1},
            products={'a': 1},
            priority=3
        ),
    ]

    system = ReactionSystem(reactions)
    final_state = system.run(state)

    print("Final state:")
    for k, v in final_state.items():
        print(f"  {k}: {v}")

    print(f"\nExpected y = 2^{x0} = {2**x0}")


if __name__ == "__main__":
    main()
