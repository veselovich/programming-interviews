import collections
import random
import time


class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]

    # Checks if A can be placed in front of B.
    @staticmethod
    def valid_placement_exists(A, B):
        return all(a < b
                   for a, b in zip(sorted(A._players), sorted(B._players)))


def main():
    start_time = time.time()

    #test case
    t = [175, 158, 201, 203, 193, 205, 166, 210, 189, 195, 178]
    team_A = Team(t)
    team_B = Team([h + 5 for h in t])

    print(Team.valid_placement_exists(team_A, team_B))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()